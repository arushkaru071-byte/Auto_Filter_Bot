from pyrogram import Client
from pyrogram.types import InlineQueryResultCachedDocument

# Correct import
from database.ia_filterdb import get_search_results


@Client.on_inline_query()
async def inline_query_handler(client, query):
    search = query.query.strip()
    if not search:
        return

    try:
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

        await query.answer(
            results,
            cache_time=0,
            is_personal=True
        )

    except Exception as e:
        print("INLINE ERROR:", e)
