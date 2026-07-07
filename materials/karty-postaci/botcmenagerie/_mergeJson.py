from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable


class DirectoryScanner:
    def __init__(self, directoryPath: Path) -> None:
        self.directoryPath = directoryPath

    def getJsonFiles(self) -> list[Path]:
        return sorted(
            [item for item in self.directoryPath.iterdir() if item.is_file() and item.suffix.lower() == '.json'],
            key=lambda path: path.name,
        )


class JsonFileLoader:
    @staticmethod
    def loadJsonAsText(filePath: Path) -> str:
        return filePath.read_text(encoding='utf-8').strip()


class OutputFileBuilder:
    @staticmethod
    def buildOutputFileName(directoryPath: Path) -> Path:
        # datestamp: str = datetime.now().strftime()
        timestamp: str = datetime.now().strftime('%Y%m%d_%H%M%S')
        fileName = f"{directoryPath.name}_{timestamp}.json"
        return directoryPath / fileName


class JsonFileWriter:
    @staticmethod
    def writeCombinedJson(outputPath: Path, jsonTexts: Iterable[str]) -> None:
        outputPath.write_text(JsonFileWriter.buildJsonArray(jsonTexts), encoding='utf-8')

    @staticmethod
    def buildJsonArray(jsonTexts: Iterable[str]) -> str:
        items = [text for text in jsonTexts if text]
        innerContent = ',\n'.join(items)
        return f"[\n{innerContent}\n]" if items else '[]'


class JsonMerger:
    def __init__(self, sourceDirectory: Path) -> None:
        self.sourceDirectory = sourceDirectory
        self.scanner = DirectoryScanner(sourceDirectory)
        self.loader = JsonFileLoader()
        self.writer = JsonFileWriter()
        self.outputPath = OutputFileBuilder.buildOutputFileName(sourceDirectory)

    def merge(self) -> Path:
        jsonFiles = self.scanner.getJsonFiles()
        jsonTexts = [self.loader.loadJsonAsText(jsonFile) for jsonFile in jsonFiles]
        self.writer.writeCombinedJson(self.outputPath, jsonTexts)
        return self.outputPath


def main() -> None:
    currentDirectory = Path(__file__).resolve().parent
    print(f"{currentDirectory=}")
    merger = JsonMerger(currentDirectory)
    outputPath = merger.merge()
    print(f'Created combined JSON file: {outputPath.name}')


if __name__ == '__main__':
    main()
