def sequence_sum(begin_number, end_number, step):
    lst = []
    if begin_number > end_number:
        return 0
    else:
          for i in range(begin_number, end_number + 1 , step):
                lst.append(i)
          return sum(lst)