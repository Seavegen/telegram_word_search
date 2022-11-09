
from asyncio import sleep, get_event_loop
from telethon import TelegramClient


api_id = 1
api_hash = "123"
client = TelegramClient('anon', api_id, api_hash)


async def parsing_entity_in_chats(client: TelegramClient) -> set:
    # старт клиента
    await client.start()
    print('start client')
    url_group = 'https://t.me/wbofficialchat'
    await client.get_participants(url_group)
    print('Получил все сущности')
    # ищем смски
    tuple_users = set()
    count = 0
    async for message in client.iter_messages(
            entity=url_group,
            search='продвижение',
            limit=156,
            wait_time=2
    ):
        # выделяем только с типом User, желательно реализовать
        # if isinstance(message.from_id.user_id, types.User):

        self_user = message.from_id.user_id
    # если нет, User объекта, то мы его пропускаем.
        if not self_user:
            continue
        # выводим сущности по типу User
        try:
            parsing_entity = await client.get_entity(self_user)
            await sleep(2)
            count += 1
            print(f'[{count}] Получена сущность: {parsing_entity.id} {parsing_entity.first_name} {parsing_entity.last_name}')
            connteinery = parsing_entity.id, parsing_entity.access_hash,parsing_entity.username
            tuple_users.add(connteinery)
        except ValueError:
            print(f'[{count}] Сущность не получена не валидный id или access_hash')
        except TypeError:
            print(f'[{count}] Нет сущности User')
    return tuple_users



async def main() -> None:
    await parsing_entity_in_chats(client)



if __name__ == '__main__':
    try:
        loop = get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('exit program')