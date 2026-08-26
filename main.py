import os
import sys

from google import genai


def main() -> None:
    """Gọi Gemini API và in câu trả lời ra log của GitHub Actions."""
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print(
            "Lỗi: Chưa thiết lập GEMINI_API_KEY trong GitHub Secrets.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Viết một câu chào ngắn gọn và tràn đầy năng lượng cho ngày mới.",
        )

        print("--- KẾT QUẢ TỪ GEMINI API ---")
        print(response.text or "Gemini không trả về nội dung văn bản.")
        print("----------------------------")
    except Exception as error:
        print(f"Lỗi khi gọi Gemini API: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
