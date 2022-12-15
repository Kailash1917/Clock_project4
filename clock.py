class Clock:
    def __init__(self, hours : int, minutes : int):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        formatted_hour = self.hours
        formatted_min = self.minutes
        if formatted_hour >= 0:
            if formatted_hour > 24:
                if formatted_min >= 0:
                    if formatted_min > 60:
                        formatted_hour = formatted_hour // 24 + formatted_min//60
                        if formatted_hour > 24:
                            formatted_hour = (formatted_hour%24) + 1
                        formatted_min %= 60
                        if formatted_min == 0:
                            formatted_hour = 0
                        if formatted_hour < 10 :
                            formatted_hour = "0" + str(formatted_hour)
                        else:
                            formatted_hour = formatted_hour
                        if formatted_min < 10:
                            formatted_min = "0" + str(formatted_min)
                        else:
                            formatted_min = formatted_min


                    elif formatted_min == 60:
                        pass

                    else:
                        formatted_hour %= 24
                        if formatted_hour < 10 :
                            formatted_hour = "0" + str(formatted_hour)
                        else:
                            formatted_hour = formatted_hour
                        if  formatted_min < 10:
                            formatted_min = "0" + str(formatted_min)
                        else:
                            formatted_min = formatted_min

                else:
                    pass

            elif formatted_hour == 24:
                if formatted_min >= 0:
                    if formatted_min > 60:
                        pass

                    elif formatted_min == 60:
                        pass

                    else:
                        formatted_hour = 0
                        if formatted_hour < 10 :
                            formatted_hour = "0" + str(formatted_hour)
                        else:
                            formatted_hour = formatted_hour
                        if  formatted_min < 10:
                            formatted_min = "0" + str(formatted_min)
                        else:
                            formatted_min = formatted_min

            else:
                if formatted_min >= 0:
                    if formatted_min > 60:
                        formatted_hour += formatted_min // 60
                        if formatted_hour > 24:
                            formatted_hour -= 24
                        formatted_min %= 60
                        if formatted_hour < 10 :
                            formatted_hour = "0" + str(formatted_hour)
                        else:
                            formatted_hour = formatted_hour
                        if formatted_min < 10:
                            formatted_min = "0" + str(formatted_min)
                        else:
                            formatted_min = formatted_min

                    elif formatted_min == 60:
                        formatted_min %= 60
                        formatted_hour = int(formatted_hour) + 1
                        if formatted_hour < 10 :
                            formatted_hour = "0" + str(formatted_hour)
                        else:
                            formatted_hour = formatted_hour
                        if formatted_min < 10:
                            formatted_min = "0" + str(formatted_min)
                        else:
                            formatted_min = formatted_min

                    else:
                        if formatted_hour < 10 :
                            formatted_hour = "0" + str(formatted_hour)
                        else:
                            formatted_hour = formatted_hour
                        if formatted_min < 10:
                            formatted_min = "0" + str(formatted_min)
                        else:
                            formatted_min = formatted_min


        else:
            if formatted_min >= 0:
                formatted_hour += 24
                if formatted_hour < 10:
                    formatted_hour = "0" + str(formatted_hour)
                else:
                    formatted_hour = formatted_hour
                if formatted_min < 10:
                    formatted_min = "0" + str(formatted_min)
                else:
                    formatted_min = formatted_min

        return "{h}:{m}".format(h=formatted_hour, m=formatted_min)

    def __lt__(self, other):
        return self.hours < other.hours

    def __gt__(self, other):
        return self.minutes > other.minutes

    def __ge__(self, other):
        return self.hours >= other.hours

    def __le__(self, other):
        return self.hours <= other.hours

    def __eq__(self, other):
         return self.hours == other.hours

    def __ne__(self, other):
        return self.hours != other.hours
    def __add__(self, other):
        return self.minutes + other