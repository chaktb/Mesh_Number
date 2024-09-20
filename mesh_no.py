import numpy as np
import matplotlib.pyplot as plt

def calculate_mesh_from_micron(micron_size):
    """
    주어진 연마재 입자 크기(마이크론)에 대해 MESH 넘버를 계산하는 함수.
    
    Parameters:
    micron_size (float): 연마재 입자 크기 (micron 단위)
    
    Returns:
    float: 계산된 MESH 넘버
    """
    if micron_size <= 0:
        raise ValueError("Micron size must be greater than 0.")
    
    mesh_number = 15000 / micron_size
    return mesh_number
def calculate_micron_from_mesh(mesh_number):
    """
    주어진 MESH 넘버에 대해 연마재 입자 크기(마이크론)를 계산하는 함수.
    
    Parameters:
    mesh_number (float): MESH 넘버
    
    Returns:
    float: 계산된 연마재 입자 크기 (micron 단위)
    """
    if mesh_number <= 0:
        raise ValueError("MESH number must be greater than 0.")
    
    micron_size = 15000 / mesh_number
    return micron_size

# 예시 실행
mesh_number = 600  # MESH 넘버 예시
micron_size = calculate_micron_from_mesh(mesh_number)
print(f"MESH 넘버 {mesh_number}에 해당하는 연마재 입자 크기는: {micron_size} µm")
mesh_number = 1000  # MESH 넘버 예시
micron_size = calculate_micron_from_mesh(mesh_number)
print(f"MESH 넘버 {mesh_number}에 해당하는 연마재 입자 크기는: {micron_size} µm")
mesh_number = 2000  # MESH 넘버 예시
micron_size = calculate_micron_from_mesh(mesh_number)
print(f"MESH 넘버 {mesh_number}에 해당하는 연마재 입자 크기는: {micron_size} µm")
# 예시 실행
# micron_size = 10  # 연마재 입자 크기 예시 (micron)
# mesh_number = calculate_mesh_from_micron(micron_size)
# print(f"입자 크기 {micron_size} µm에 해당하는 MESH 넘버는: {mesh_number}")



# MESH 넘버 범위 설정
mesh_numbers = np.arange(100, 1000, 10)  # 10에서 400까지 MESH 넘버 설정

# MESH 넘버에 따른 연마재 크기 (micron) 계산
micron_sizes = 15000 / mesh_numbers

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(mesh_numbers, micron_sizes, marker='o', linestyle='-', color='b')
plt.title('MESH Number vs Abrasive Particle Size (Micron)')
plt.xlabel('MESH Number')
plt.ylabel('Abrasive Particle Size (Micron)')
plt.grid(True)
# plt.xscale('log')  # MESH 넘버는 로그 스케일로 표시
plt.xscale('linear')  # MESH 넘버는 로그 스케일로 표시
plt.yscale('log')  # 입자 크기도 로그 스케일로 표시
plt.show()