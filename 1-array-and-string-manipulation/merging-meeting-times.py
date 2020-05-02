def merge_ranges(meetings):
    new_list = []
    merged_meetings = set()
    for current_meeting_idx in range(len(meetings)):
        if (current_meeting_idx in merged_meetings):
            continue
        start = meetings[current_meeting_idx][0]
        end = meetings[current_meeting_idx][1]
        merged_meetings.add(current_meeting_idx)
        for other_meeting_idx in range(current_meeting_idx+1, len(meetings)):
            if (other_meeting_idx in merged_meetings):
                continue
            if start > meetings[other_meeting_idx][0] and meetings[other_meeting_idx][1] <= end:
                start = meetings[other_meeting_idx][0]
                merged_meetings.add(other_meeting_idx)
            if end >= meetings[other_meeting_idx][0] and meetings[other_meeting_idx][1] > end:
                end = meetings[other_meeting_idx][1]
                merged_meetings.add(other_meeting_idx)
        new_tuple = (start, end)
        new_list.append(new_tuple)
    return new_list

print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))  