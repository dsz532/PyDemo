class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        Kelvin=celsius+273.15
        Fahrenheit=celsius*1.80+32.00
        result=[Kelvin,Fahrenheit]
        return result
pass

solution=Solution()
celsius = 36.50
print(solution.convertTemperature(celsius))