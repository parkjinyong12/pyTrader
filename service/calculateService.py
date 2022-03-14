from datetime import datetime, timedelta, date
import exchange_calendars as xcals

class CalculateService:

    def __init__(self):
        # print("hello CalculateService..")
        pass
        
    # 효율성 비율 계산(input:내림차순 정렬 데이터)
    def get_efficiency_ratio_from_descending_data(self, seriesData, period):
        if period >= seriesData.size:
            #print("series size:",seriesData.size,"pass..")
            return 0

        # 인덱스
        start_index=0      
        end_index=start_index+period-1   

        # volatility
        deviation_sum = 0

        for idx in range(0, end_index):
            today_val = seriesData[idx]
            yesterday_val = seriesData[idx+1]
            deviation_sum = deviation_sum + abs(today_val - yesterday_val)

        # gap
        now_val = seriesData[start_index]
        past_val = seriesData[end_index]
        gap = now_val - past_val

        efficiency_ratio = 0

        # 분모가 0이 아니면
        if(deviation_sum != 0):
            efficiency_ratio = gap / deviation_sum
            efficiency_ratio = round(efficiency_ratio, 6)

        #print("start",past_val,"end",now_val,"gap",gap,"volatility",deviation_sum,"er",efficiency_ratio)
        
        # er 계산
        return efficiency_ratio

    # 효율성 비율 계산
    def get_efficiency_ratio(self, data_list):

        # 인덱스
        start_index=0      
        end_index=len(data_list)

        # volatility
        deviation_sum = 0

        data_list_index = 0
        before_one_val = 0

        # 마지막 행 제외
        for index in range(start_index, end_index-1):
            # print(data_list[index+1][0] - data_list[index][0])
            deviation_sum = deviation_sum + abs(data_list[index+1][0] - data_list[index][0])

        # 20210907 ~ 20220206 - 100개
        
        # gap
        start_val = data_list[start_index][0]
        end_val = data_list[end_index-1][0]
        
        gap = end_val - start_val

        efficiency_ratio = 0

        # 분모가 0이 아니면
        if(deviation_sum != 0):
            efficiency_ratio = gap / deviation_sum
            efficiency_ratio = round(efficiency_ratio, 6)

        # print("gap",gap,"volatility",deviation_sum,"er",efficiency_ratio)
        
        # er 계산
        return efficiency_ratio

    # 일 평균 상승율 계산
    def get_avg_rate_of_rise_by_days(self, data_list):

        # 인덱스
        start_index=0      
        len_data_list=len(data_list)
        
        # gap
        start_val = data_list[start_index][0]
        end_val = data_list[len_data_list-1][0]
        
        gap = end_val - start_val

        avg_rate_of_rise = 0

        # 분모가 0이 아니면
        if(len_data_list != 0):
            avg_rate_of_rise = gap / len_data_list
            avg_rate_of_rise = round(avg_rate_of_rise, 6)

        # print("start",start_val,"end",end_val,"avg",avg_rate_of_rise)
        # avg 계산
        return avg_rate_of_rise

    # 기간의 시작일과 종료일 계산
    def get_start_day_from_today_for_weeks(self, weeks):
        days = {}
        now = datetime.now()
        today = now.strftime('%Y%m%d')
        days["end"] = today
        before_weeks = now - timedelta(weeks=weeks)
        before_weeks_day = before_weeks.strftime('%Y%m%d')
        days["start"] = before_weeks_day
        return days

    # 기간의 시작일과 종료일 계산
    def get_start_day_from_end_day_for_weeks(self, end_day, weeks):
        start_day = datetime.strptime(end_day,'%Y%m%d')-timedelta(weeks=weeks)
        return start_day.strftime('%Y%m%d')

    def get_start_business_day_before_days(self, end_day, days):
        
        xkrx = xcals.get_calendar("XKRX")
        previous_day = end_day
        for day in range(0, days):
            previous_day = xkrx.previous_session(previous_day).strftime('%Y%m%d')

        return previous_day

    def get_today_yyyymmdd(self):
        now = datetime.now()
        return now.strftime('%Y%m%d')