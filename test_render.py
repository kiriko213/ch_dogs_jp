import asyncio
import json
from generate_video import make_short_video

async def main():
    print("ローカルでのテストレンダリングを開始します（YouTubeにはアップロードされません）")
    
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    p = config["hamsters_jp"]
    
    # テスト用の短い台本
    script = """
    【Hook】ハムスターの意外な秘密、知ってる？
    【Insight】実はハムスターは、一晩で数キロも走るスタミナの持ち主なんです！小さな体のどこにそんなパワーが！？
    【CTA】ハムちゃんが喜ぶアイテム、プロフィールに置いてます。
    PexelsKeyword: cute hamster
    """
    
    try:
        output_file = await make_short_video(
            script, 
            'bg.jpg', 
            'bgm.mp3', 
            "test_hamster_output.mp4",
            voice=p['voice'],
            pexels_key=p.get('pexels_api_key'),
            topic="hamsters_jp", 
            pexels_query="cute hamster"
        )
        print(f"\n✅ テスト動画の生成が完了しました！")
        print(f"このフォルダにある '{output_file}' をダブルクリックして再生して確認してください。")
        print("YouTubeのアップロード枠（クォータ）は一切消費していません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    asyncio.run(main())
