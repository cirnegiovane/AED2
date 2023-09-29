def process_files(test_cases):
    for i in range(test_cases):
        k, m = map(int, input("k/m: ").split())
        files = []
        for j in range(m):
            crit, size = map(int, input(f"crit/size {j}: ").split())
            files.append((crit, size))
        
        files.sort(reverse=True)
        
        total_size = 0
        num_files = 0
        
        for crit, size in files:
            if total_size + size <= k:
                total_size += size
                num_files += 1
        
        print(num_files)


num_test_cases = int(input("Num casos de teste:"))

process_files(num_test_cases)