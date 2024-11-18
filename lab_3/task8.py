hour = int(input("Час початку (години): "))
mins = int(input("Час початку (хвилини): "))
dura = int(input("Тривалість (хвилини): "))

total_minutes = hour * 60 + mins + dura

end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

print(f"Подія закінчиться: {end_hour}:{end_minute}")
