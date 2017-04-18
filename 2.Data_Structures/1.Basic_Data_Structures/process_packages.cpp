#include <iostream>
#include <queue>
#include <vector>

struct Request {
    Request(int arrival_time, int process_time):
        arrival_time(arrival_time),
        process_time(process_time)
    {}

    int arrival_time;
    int process_time;
};

struct Response {
    Response(bool dropped, int start_time):
        dropped(dropped),
        start_time(start_time)
    {}

    bool dropped;
    int start_time;
};

class Buffer {
public:
    Buffer(int size):
        size_(size),
        finish_time_()
    {}

    Response Process(const Request &request) {
        // write your code here
        int fin = 0;
        Response re(1,0);

        if (!finish_time_.empty()) {
          //We already have some elements in processing
          while (finish_time_.front() <= request.arrival_time && (!finish_time_.empty())) {

            //Pop all the tasks that have actually finished when the present packet has entered
            fin = finish_time_.front();
            finish_time_.pop();
          }
          if (finish_time_.size() == size_) {
            //The buffer is already full, packet to be dropped
            re.dropped = 1;
            return re;
          }
          if (finish_time_.empty()) {
            //If the buffer becomes completely empty after the processing
            //of previous packets.
            //If buffer is empty, the response start time will be same as arrival_time
            re.start_time = request.arrival_time;
            //The finish time will be the ending time of the
            //last packet in buffer + process_time of present packet
            finish_time_.push(fin + request.process_time);
          }
          else {
            //Nothing in queue for processing at time of entry of present packet
            //The response start time will be same as when the last item in
            //buffer will finish processing
            re.start_time = finish_time_.back();
            finish_time_.push(finish_time_.back() + request.process_time);

          }
          //If we come here, then the packet will not be dropped
          re.dropped = 0;
          //re.start_time = finish_time_.back();
          return re;
        }
        else {
          /* At the time the packet comes in the buffer is
          completely empty, so computer is idle. The start_time will be
          same as the arrival_time. The finish_time will
          be arrival_time + process_time
          */
          finish_time_.push(request.arrival_time + request.process_time);
          re.dropped = 0;
          re.start_time = request.arrival_time;
          return re;
        }
    }
private:
    int size_;
    std::queue <int> finish_time_;
};

std::vector <Request> ReadRequests() {
    std::vector <Request> requests;
    int count;
    std::cin >> count;
    for (int i = 0; i < count; ++i) {
        int arrival_time, process_time;
        std::cin >> arrival_time >> process_time;
        requests.push_back(Request(arrival_time, process_time));
    }
    return requests;
}

std::vector <Response> ProcessRequests(const std::vector <Request> &requests, Buffer *buffer) {
    std::vector<Response> responses;
    for (int i = 0; i < requests.size(); ++i)
        responses.push_back(buffer->Process(requests[i]));
    return responses;
}

void PrintResponses(const std::vector <Response> &responses) {
    for (int i = 0; i < responses.size(); ++i)
        std::cout << (responses[i].dropped ? -1 : responses[i].start_time) << std::endl;
}

int main() {
    int size;
    std::cin >> size;
    std::vector <Request> requests = ReadRequests();

    Buffer buffer(size);
    std::vector <Response> responses = ProcessRequests(requests, &buffer);

    PrintResponses(responses);
    return 0;
}
