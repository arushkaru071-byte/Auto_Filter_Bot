from pyrogram import Client
from pyrogram.types import InlineQueryResultCachedDocument

from database.ia_filter import get_search_results   # ✅ Correct import!

@Client.on_inline_query()
async def inline_query_handler(client, query):

    search = query.query.strip()
    if not search:
        return

    files, _, _ = await get_search_results(
        chat_id=None,
        query=search
    )

    results = []
    for file in files:
        results.append(
            InlineQueryResultCachedDocument(
                title=file.file_name,
                document_file_id=file.file_id
            )
        )

    try:
        await query.answer(
            results,
            cache_time=0,
            is_personal=True
        )
    except Exception as e:
        print("INLINE ERROR:", e)
