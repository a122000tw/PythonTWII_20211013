def get_rabbit_and_chicken(amount, feet):
    if amount * 2 <= feet <= amount * 4:
        rabbit = (feet - 2 * amount) / 2
        chicken = amount - rabbit
        print('兔子:', rabbit, '雞:', chicken)
    else:
        print('amount:', amount, 'feet:', feet, '設定不正確')

    return rabbit, chicken


if __name__ == '__main__':
    get_rabbit_and_chicken(83, 240)
