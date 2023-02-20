class Solution:
    def solveEquation(self, equation):
        left,right = equation.split('=')
        ln=[]
        lv=[]
        rn=[]
        rv=[]


        i=0
        status=False
        temp=''
        while i<len(left):
            if left[i] == '-':
                if temp!='':
                    ln.append(int(temp))
                    temp=''
                    if status:
                        rn[-1]=-rn[-1]
                status = True
            elif left[i] == '+':
                if left[i-1]!='x':
                    if not status:
                        ln.append(int(temp))
                    else:
                        ln.append(-int(temp))
                        status=False
                    temp=''
            elif left[i] == 'x':
                if temp == '':
                    lv.append(1)
                else:
                    lv.append(int(temp))
                    temp = ''
                if status:
                    lv[-1] = -lv[-1]
                    status=False
            else:
                temp+=left[i]
            i+=1
        if temp!='':
            ln.append(int(temp))
            if status:
                ln[-1] = -ln[-1]

        i = 0
        status = False
        temp = ''
        while i < len(right):
            if right[i] == '-':
                if temp != '':
                    rn.append(int(temp))
                    temp = ''
                    if status:
                        rn[-1]=-rn[-1]
                status = True
            elif right[i] == '+':
                if right[i - 1] != 'x':
                    if not status:
                        rn.append(int(temp))
                    else:
                        rn.append(-int(temp))
                        status = False
                    temp = ''
            elif right[i] == 'x':
                if temp == '':
                    rv.append(1)
                else:
                    rv.append(int(temp))
                    temp = ''
                if status:
                    rv[-1] = -rv[-1]
                    status = False
            else:
                temp += right[i]
            i += 1
        if temp != '':
            rn.append(int(temp))
            if status:
                rn[-1] = -rn[-1]

        a = sum(ln)
        b = sum(lv)
        c = sum(rn)
        d = sum(rv)
        print(a,b,c,d)

        if a==c and b==d:
            return 'Infinite solutions'
        try:
            return 'x='+str( (c-a)//(b-d) )
        except:
            return 'No solution'



ans = Solution()
equation = "x+5-3+x=6+x-2"
print(ans.solveEquation(equation))