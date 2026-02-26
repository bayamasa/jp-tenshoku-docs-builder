.PHONY: setup test lint build-wh-standard build-wh-star build-resume sample-wh-standard sample-wh-star sample-resume clean docker-build docker-run-wh-standard docker-run-wh-star docker-run-resume

# セットアップ
setup:
	uv sync

# テスト
test:
	uv run pytest tests/ -v

# リント
lint:
	uv run ruff check src/ tests/

# 職務経歴書（標準） - .personal/ の個人情報を使用してPDF生成
build-wh-standard:
	@mkdir -p output
	uv run python -m jp_tenshoku_docs_builder .personal/work_history_standard.yaml -c .personal/credential.yaml -o output/work-history-standard.pdf

# 職務経歴書（STAR法） - .personal/ の個人情報を使用してPDF生成
build-wh-star:
	@mkdir -p output
	uv run python -m jp_tenshoku_docs_builder .personal/work_history_star.yaml -c .personal/credential.yaml -o output/work-history-star.pdf --format star

# 履歴書 - .personal/ の個人情報を使用してPDF生成
build-resume:
	@mkdir -p output
	uv run python -m jp_tenshoku_docs_builder .personal/resume.yaml -c .personal/credential.yaml -o output/resume.pdf --type resume

# サンプルPDF生成（sample/ のダミーデータを使用）
sample-wh-standard:
	@mkdir -p output
	uv run python -m jp_tenshoku_docs_builder sample/work_history_standard.yaml -c sample/credential.yaml -o output/work-history-standard-sample.pdf

sample-wh-star:
	@mkdir -p output
	uv run python -m jp_tenshoku_docs_builder sample/work_history_star.yaml -c sample/credential.yaml -o output/work-history-star-sample.pdf --format star

sample-resume:
	@mkdir -p output
	uv run python -m jp_tenshoku_docs_builder sample/resume.yaml -c sample/credential.yaml -o output/resume-sample.pdf --type resume

# Docker
docker-build:
	docker build -t jp-tenshoku-docs-builder .

docker-run-wh-standard: docker-build
	docker run --rm -v "$(PWD)":/work jp-tenshoku-docs-builder /work/sample/work_history_standard.yaml -c /work/sample/credential.yaml -o /work/output/work-history-standard.pdf

docker-run-wh-star: docker-build
	docker run --rm -v "$(PWD)":/work jp-tenshoku-docs-builder /work/sample/work_history_star.yaml -c /work/sample/credential.yaml -o /work/output/work-history-star.pdf --format star

docker-run-resume: docker-build
	docker run --rm -v "$(PWD)":/work jp-tenshoku-docs-builder /work/sample/resume.yaml -c /work/sample/credential.yaml -o /work/output/resume.pdf --type resume

# クリーンアップ
clean:
	rm -rf output/
