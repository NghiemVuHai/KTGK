def bubble_sort(arr):
    
    n = len(arr)
    
   
    for i in range(n):
       
        swapped = False
        
        
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        
        if not swapped:
            break
            
    return arr

def main():
    try:
       
        input_str = input("Nhập vào các số nguyên, cách nhau bởi dấu cách: ")
        arr = [int(x) for x in input_str.split()]
        
        if not arr:
            print("Mảng trống!")
            return
            
       
        sorted_arr = bubble_sort(arr.copy())
        
     
        print("Mảng trước khi sắp xếp:", arr)
        print("Mảng sau khi sắp xếp:", sorted_arr)
        
    except ValueError:
        print("Vui lòng nhập các số nguyên hợp lệ.")

if __name__ == "__main__":
    main()