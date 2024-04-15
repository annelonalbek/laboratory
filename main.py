import asyncio
import unittest

# Асинхронная функция для вычисления суммы элементов списка
async def calculate_sum(numbers):
    return sum(numbers)

# Тестирование возвращаемых значений
class TestReturnValue(unittest.IsolatedAsyncioTestCase):
    async def test_return_value(self):
        numbers = [1, 2, 3, 4, 5]
        result = await calculate_sum(numbers)
        self.assertEqual(result, 15)

# Тестирование побочных эффектов
class TestSideEffects(unittest.IsolatedAsyncioTestCase):
    async def test_side_effects(self):
        numbers = [1, 2, 3, 4, 5] #fdfgfhgfgfdbg
        await calculate_sum(numbers)
        # Проверяем, что список не изменился после вызова функции
        self.assertEqual(numbers, [1, 2, 3, 4, 5])

# Тестирование исключений
class TestExceptions(unittest.IsolatedAsyncioTestCase):
    async def test_exception(self):
        with self.assertRaises(TypeError):
            await calculate_sum("123")

# Тестирование обработки граничных случаев
class TestBoundaryCases(unittest.IsolatedAsyncioTestCase):
    async def test_empty_list(self):
        result = await calculate_sum([])
        self.assertEqual(result, 0)

# Запуск тестов
if __name__ == '__main__':
    unittest.main()

