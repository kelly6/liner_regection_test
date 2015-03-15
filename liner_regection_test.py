#!/bin/bash
# -*- coding:utf-8 -*-

class liner_reg():
    def __init__(self):
        #self.train_data = [((1, 1,),1), ((1, 2,),2), ((1, 3,),3), ((1, 4,),4), ((1, 5,),5)]
        self.x = [(1, i) for i in range(1, 6)]
        self.y = range(1, 6)
        self.n = len(self.x[0])
        self.m = len(self.x)
        self.theta_list = [0] * self.n
        self.arg_limit = 0.0001
        self.loop_max = 1000

    def J_theta(self):
        pass

    def h_theta_x(self, i):
        for j in range(len(self.x[i])):
            continue
            print self.theta_list[j] * self.x[i][j]
        l = [self.theta_list[j] * self.x[i][j] for j in range(len(self.x[i]))]
        return sum(l)

    def conv_theta_old(self, i, alpha):
        if i:
            sums = 0.0
            for idx in range(self.m):
                print self.h_theta_x(idx), self.y[idx], self.x[idx][i]
                sums += (self.h_theta_x(idx) - self.y[idx]) * self.x[idx][i]
                break
            step = alpha * sums
            temp_theta = self.theta_list[i] - step
            print "temp_theta[%d]:%f, step:%f, sums:%f" % (i, temp_theta, step, sums)
            self.theta_list[i] = temp_theta
            if abs(step) < 0.001:
                return 1
            return 0
        else:
            return 1

    def conv_theta(self, alpha):
        not_all_done = 0
        for i in range(self.m):
            diff = self.h_theta_x(i) - self.y[i]
            for j in range(self.n):
                tmp_thetan = self.theta_list[j] - alpha * diff * self.x[i][j]
                mins = abs(self.theta_list[j] - tmp_thetan)
                if abs(self.theta_list[j] - tmp_thetan) > self.arg_limit:
                    not_all_done = 1
                self.theta_list[j] = tmp_thetan
            print self.theta_list, diff
            print mins
        return not_all_done
if __name__ == "__main__":
    l = liner_reg()
    counter = 0
    while counter < l.loop_max:
        counter += 1
        ret = l.conv_theta(0.01)
        if not ret:
            break
    print "liner regection done.", counter
    exit()
    for i in range(len(l.theta_list)):
        counter = 0
        print "-" * 80
        while not l.conv_theta(i, 0.1):
            print l.theta_list
            counter += 1
            if counter > 10:
                break
        print "-" * 80
