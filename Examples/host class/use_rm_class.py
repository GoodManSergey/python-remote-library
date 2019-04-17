from host.host_class import Class


if __name__ == '__main__':
    cl = Class("127.0.0.1", "8080")

    print(cl.a_plus_b(a=12, b=77))
    print(cl.a_multiply_b(2, 2))
    print(cl.return_b_y())
