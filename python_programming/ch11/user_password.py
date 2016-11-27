# -*- coding: utf-8 -*-
# 비밀번호 정합성 체크를 위한 함
def password_validation_check(pwd):
    """ checking password validation

    Args:
        pwd (str) : password string

    Return:
        True or False (boolean) : the result of checking validation
    """
    pass

    # 비밀번호 길이 확인(6~12)
    if len(pwd) < 6 or len(pwd) > 12:
        print(pwd, '의 길이가 적당하지 않습니다.')
        return False

    print(pwd, '는 비밀번호로 적당합니다!')
    return True

if __name__ == '__main__':
    password_validation_check('23kje')
    password_validation_check('432rewvb53')
