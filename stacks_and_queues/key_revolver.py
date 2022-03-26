from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())
index = 0
used_bullets = 0
while bullets and locks:

    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet > current_lock:
        print('Ping!')
        locks.appendleft(current_lock)
    else:
        print('Bang!')
    used_bullets += 1
    index += 1
    if index != 0 and index % gun_barrel_size == 0 and bullets:
        print('Reloading!')
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    cost = used_bullets * bullet_price
    money_earned = intelligence_value - cost
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
