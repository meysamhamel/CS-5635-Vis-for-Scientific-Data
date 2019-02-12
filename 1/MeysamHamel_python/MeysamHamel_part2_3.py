
#Meysam HamelS
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read_csv(filename, header_row):
    df = pd.read_csv(filename, header=header_row)
    A = df.as_matrix()
    year = A[:, 0]
    month = A[:, 1]
    date_m = A[:, 2]
    day_of_week = A[:, 3]
    births = A[:, 4]
    return df, year, month, date_m, day_of_week, births


def calc__d():
    df, year, month, date_m, day_of_week, births = read_csv("US_births_2000-2014_SSA.csv", 0)
    sun_c = 0
    mon_c = 0
    tue_c = 0
    wed_c = 0
    thu_c = 0
    fri_c = 0
    sat_c = 0

    c_1 = 0
    c_2 = 0
    c_3 = 0
    c_4 = 0
    c_5 = 0
    c_6 = 0
    c_7 = 0
    c_8 = 0
    c_9 = 0
    c_10 = 0
    c_11 = 0
    c_12 = 0
    c_13 = 0
    c_14 = 0
    c_15 = 0
    c_16 = 0
    c_17 = 0
    c_18 = 0
    c_19 = 0
    c_20 = 0
    c_21 = 0
    c_22 = 0
    c_23 = 0
    c_24 = 0
    c_25 = 0
    c_26 = 0
    c_27 = 0
    c_28 = 0
    c_29 = 0
    c_30 = 0
    c_31 = 0

    jan_c = 0
    feb_c = 0
    mar_c = 0
    apr_c = 0
    may_c = 0
    jun_c = 0
    jul_c = 0
    aug_c = 0
    sep_c = 0
    oct_c = 0
    nov_c = 0
    dec_c = 0

    for x in range(0, len(year)):
     
        if day_of_week[x] == 1:
            sun_c += births[x]
        elif day_of_week[x] == 2:
            mon_c += births[x]
        elif day_of_week[x] == 3:
            tue_c += births[x]
        elif day_of_week[x] == 4:
            wed_c += births[x]
        elif day_of_week[x] == 5:
            thu_c += births[x]
        elif day_of_week[x] == 6:
            fri_c += births[x]
        elif day_of_week[x] == 7:
            sat_c += births[x]

        #  Count which day of the month they were born.
        if date_m[x] == 1:
            c_1 += births[x]
        elif date_m[x] == 2:
            c_2 += births[x]
        elif date_m[x] == 2:
            c_2 += births[x]
        elif date_m[x] == 3:
            c_3 += births[x]
        elif date_m[x] == 4:
            c_4 += births[x]
        elif date_m[x] == 5:
            c_5 += births[x]
        elif date_m[x] == 6:
            c_6 += births[x]
        elif date_m[x] == 7:
            c_7 += births[x]
        elif date_m[x] == 8:
            c_8 += births[x]
        elif date_m[x] == 9:
            c_9 += births[x]
        elif date_m[x] == 10:
            c_10 += births[x]
        elif date_m[x] == 11:
            c_11 += births[x]
        elif date_m[x] == 12:
            c_12 += births[x]
        elif date_m[x] == 13:
            c_13 += births[x]
        elif date_m[x] == 14:
            c_14 += births[x]
        elif date_m[x] == 15:
            c_15 += births[x]
        elif date_m[x] == 16:
            c_16 += births[x]
        elif date_m[x] == 17:
            c_17 += births[x]
        elif date_m[x] == 18:
            c_18 += births[x]
        elif date_m[x] == 19:
            c_19 += births[x]
        elif date_m[x] == 20:
            c_20 += births[x]
        elif date_m[x] == 21:
            c_21 += births[x]
        elif date_m[x] == 22:
            c_22 += births[x]
        elif date_m[x] == 23:
            c_23 += births[x]
        elif date_m[x] == 24:
            c_24 += births[x]
        elif date_m[x] == 25:
            c_25 += births[x]
        elif date_m[x] == 26:
            c_26 += births[x]
        elif date_m[x] == 27:
            c_27 += births[x]
        elif date_m[x] == 28:
            c_28 += births[x]
        elif date_m[x] == 29:
            c_29 += births[x]
        elif date_m[x] == 30:
            c_30 += births[x]
        elif date_m[x] == 31:
            c_31 += births[x]

        if month[x] == 1:
            jan_c += births[x]
        elif month[x] == 2:
            feb_c += births[x]
        elif month[x] == 3:
            mar_c += births[x]
        elif month[x] == 4:
            apr_c += births[x]
        elif month[x] == 5:
            may_c += births[x]
        elif month[x] == 6:
            jun_c += births[x]
        elif month[x] == 7:
            jul_c += births[x]
        elif month[x] == 8:
            aug_c += births[x]
        elif month[x] == 9:
            sep_c += births[x]
        elif month[x] == 10:
            oct_c += births[x]
        elif month[x] == 11:
            nov_c += births[x]
        elif month[x] == 12:
            dec_c += births[x]

    tav_month = [c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10,
                                    c_11, c_12, c_13, c_14, c_15, c_16, c_17, c_18, c_19, c_20,
                                    c_21, c_22, c_23, c_24, c_25, c_26, c_27, c_28, c_29, c_30, c_31]
    tav_week = [sun_c, mon_c, tue_c, wed_c, thu_c, fri_c, sat_c]
    tav_mm = [jan_c, feb_c, mar_c, apr_c,
                             may_c, jun_c, jul_c, aug_c,
                             sep_c, oct_c, nov_c, dec_c]
    print(tav_month)
    return tav_month, tav_week, tav_mm


def plot__day__m(data):
    objects = []
    for i in range(1, 32):
        objects.append(i)

    y_pos = np.arange(len(objects))
    performance = []
    for i in range (31):
        performance.append(data[i])
    plt.figure(figsize=(10, 6))
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Birth counts')
    plt.title('Birth calculate by Day of Month')
    plt.show()


def draw_bar_plot_day_of_week(data):
    objects = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    y_pos = np.arange(len(objects))
    performance = [data[0], data[1], data[2], data[3], data[4], data[5], data[6]]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Birth counts')
    plt.title('Birthday calculate by day')
    plt.show()


def plot__month(data):
    objects = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    y_pos = np.arange(len(objects))
    performance = []
    for i in range(12):
        performance.append(data[i])
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Birth counts')
    plt.title('Birthday calculate by month')
    plt.show()


def main():
    tav_month, tav_week, tav_mm = calc__d()
    plot__day__m(tav_month)
    draw_bar_plot_day_of_week(tav_week)
    temp_max = 0
    temp_max_index = 0
    for i in range (31):
        if temp_max < tav_month[i]:
            temp_max = tav_month[i]
            temp_max_index = i+1

    print("The day of the month with the highest number of birth was on %dth with %d births." % (temp_max_index, temp_max))

    plot__month(tav_mm)


    # plot_histogram()
    # year, value = read_csv("part2_q1.csv", 4)
    # print(year)


if __name__ == "__main__":
    main()