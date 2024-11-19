# 쌍자음 인식
if cur_res_final in double_const.keys():
    # 머신러닝 쌍자음 인식 알고리즘을 직접 구현해야 합니다.
    # 예시로는 double_const 딕셔너리를 활용한 예시를 제공합니다.
    if len(landmark_input) == 0:
        landmark_input.append(cur_res_final)
    else:
        prev_res_final = landmark_input[-1]
        if prev_res_final in double_const and double_const[prev_res_final] == cur_res_final:
            landmark_input.append(cur_res_final)
            if len(landmark_input) == 2:
                cur_res_final = landmark_input[-2]  # 이전에 저장한 값을 사용
                landmark_input.clear()
        else:
            landmark_input.clear()
