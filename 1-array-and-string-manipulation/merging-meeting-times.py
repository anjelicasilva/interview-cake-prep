# Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges. Here we've simplified our times down to the number of 30-minute slots past 9:00 am. But we want the method to work even for very large numbers, like Unix timestamps. In any case, the spirit of the challenge is to merge meetings where startTime and endTime don't have an upper bound.





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



# IC Solution

def merge_ranges(meetings):

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings