import os
from pathlib import Path


def load_filters(filter_file):
    """Загружает файлы и директории для исключения из фильтр-файла."""
    excluded_files = set()
    excluded_dirs = set()
    if os.path.exists(filter_file):
        with open(filter_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("#") or not line:  # Игнорировать комментарии и пустые строки
                    continue
                if line.startswith("dir:"):
                    excluded_dirs.add(line[4:].strip())
                elif line.startswith("file:"):
                    excluded_files.add(line[5:].strip())
    return excluded_files, excluded_dirs


def get_file_language(file_name):
    """Определяет язык программирования по расширению файла."""
    extensions = {
        '.py': 'python',
        '.js': 'javascript',
        '.json': 'json',
        '.twig': 'html twig',
        '.java': 'java',
        '.php': 'php',
        '.cs': 'csharp',
        '.html': 'html',
        '.css': 'css',
        '.sh': 'bash',
        '.md': 'markdown',
        '.rst': 'restructuredtext',
        '.txt': '',
        '.c': 'c',
        '.cpp': 'cpp',
        '.h': 'c header',
        '.hpp': 'cpp header',
        '.ts': 'typescript',
        '.tsx': 'typescript jsx',
        '.jsx': 'javascript jsx',
        '.go': 'go',
        '.rb': 'ruby',
        '.swift': 'swift',
        '.kt': 'kotlin',
        '.dart': 'dart',
        '.xml': 'xml',
        '.yml': 'yaml',
        '.yaml': 'yaml',
        '.ini': 'ini',
        '.bat': 'batch',
        '.sql': 'sql',
        '.asm': 'assembly',
        '.pl': 'perl',
        '.r': 'r',
        '.scala': 'scala',
        '.lua': 'lua',
        '.rs': 'rust',
        '.vb': 'visual basic',
        '.dockerfile': 'dockerfile',
        '.makefile': 'makefile',
        '.gradle': 'gradle',
        '.toml': 'toml',
        '.coffee': 'coffeescript',
        '.erl': 'erlang',
        '.ex': 'elixir',
        '.clj': 'clojure',
        '.groovy': 'groovy',
        '.ps1': 'powershell',
        '.awk': 'awk',
    }
    return extensions.get(Path(file_name).suffix, '')


def collect_files_content(base_dir, excluded_files, excluded_dirs, output_file):
    """Собирает содержимое файлов и записывает их в формате Markdown."""
    result = []
    base_path = Path(base_dir).resolve()

    for root, dirs, files in os.walk(base_path):
        relative_root = Path(root).relative_to(base_path)

        # Исключить директории
        dirs[:] = [d for d in dirs if not any((relative_root / d).match(pattern) for pattern in excluded_dirs)]

        for file in files:
            relative_file_path = relative_root / file

            # Исключить файлы
            if any(relative_file_path.match(pattern) for pattern in excluded_files):
                continue

            try:
                full_path = Path(root) / file
                with full_path.open("r", encoding="utf-8") as f:
                    content = f.read()

                # Пропустить пустые файлы
                if not content.strip():
                    continue

                language = get_file_language(file)
                result.append(f"`{relative_file_path}`\n```{language}\n{content}\n```")
            except Exception as e:
                print(f"Ошибка при обработке файла {file}: {e}")

    # Запись результатов в Markdown файл
    with open(output_file, "w", encoding="utf-8") as md_file:
        md_file.write("\n\n".join(result))


if __name__ == "__main__":
    base_directory = input("Введите путь к директории для обработки: ")
    filter_file = input("Введите путь к фильтр-файлу: ")

    # Получение имени директории для включения в имя файла
    target_directory_name = Path(base_directory).resolve().name
    output_markdown_file = f"output_{target_directory_name}.md"

    excluded_files, excluded_dirs = load_filters(filter_file)
    collect_files_content(base_directory, excluded_files, excluded_dirs, output_markdown_file)

    print(f"Содержимое файлов сохранено в {output_markdown_file}")
