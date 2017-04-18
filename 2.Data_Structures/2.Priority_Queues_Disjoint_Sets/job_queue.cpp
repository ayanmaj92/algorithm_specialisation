#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using std::vector;
using std::cin;
using std::cout;
using std::pair;
using std::swap;
using std::make_pair;

class JobQueue {
 private:
  unsigned long long num_workers_;
  vector<unsigned long long> jobs_;

  vector<unsigned long long> assigned_workers_;
  vector<long long> start_times_;
  vector< pair<unsigned long long,unsigned long long> > threadq;

  unsigned long long Parent(unsigned long long i) {
    return floor((i-1)/2);
  }

  unsigned long long LeftChild(unsigned long long i) {
    return (2*i + 1);
  }

  unsigned long long RightChild(unsigned long long i) {
    return (2*i + 2);
  }

  void SiftUp(unsigned long long i) {
    while (i>0 && ( (threadq[Parent(i)].second > threadq[i].second)
                  || ( (threadq[Parent(i)].second == threadq[i].second) && ( threadq[Parent(i)].first > threadq[i].first ) ) )) {
      swap(threadq[Parent(i)],threadq[i]);
      i = Parent(i);
    }
  }

  void SiftDown(unsigned long long i) {
    unsigned long long minIndex = i;
    unsigned long long l = LeftChild(i);

    if (l<threadq.size() && ( (threadq[l].second<threadq[minIndex].second)
                          || (  (threadq[l].second == threadq[minIndex].second) && ( threadq[l].first < threadq[minIndex].first )  ) )) {
        minIndex = l;
    }
    unsigned long long r = RightChild(i);
    if (r<threadq.size() && ( (threadq[r].second<threadq[minIndex].second)
                          || (  (threadq[r].second == threadq[minIndex].second) && ( threadq[r].first < threadq[minIndex].first )  ) )) {
        minIndex = r;
    }
    if (i != minIndex) {
      swap(threadq[minIndex],threadq[i]);
      SiftDown(minIndex);
    }
  }

  void Insert(pair<unsigned long long,unsigned long long> p) {
    threadq.push_back(p);
    SiftUp(threadq.size()-1);
  }

  pair<unsigned long long,unsigned long long> ExtractMin() {
    pair<unsigned long long,unsigned long long> p = threadq[0];
    swap(threadq[0], threadq[threadq.size()-1]);

    threadq.pop_back();

    SiftDown(0);

    return p;
  }

  void WriteResponse() const {
    for (unsigned long long i = 0; i < jobs_.size(); ++i) {
      cout << assigned_workers_[i] << " " << start_times_[i] << "\n";
    }
  }

  void ReadData() {
    unsigned long long m;
    cin >> num_workers_ >> m;
    jobs_.resize(m);
    for(unsigned long long i = 0; i < m; ++i)
      cin >> jobs_[i];
  }

  void AssignJobs() {
    // TODO: replace this code with a faster algorithm.
    assigned_workers_.resize(jobs_.size());
    start_times_.resize(jobs_.size());
    vector<long long> next_free_time(num_workers_, 0);
    unsigned long long i;
    unsigned long long lim1 = (num_workers_<=jobs_.size())?num_workers_:jobs_.size();
    for (i = 0; i < lim1; i++) {
      unsigned long long duration = jobs_[i];
      pair<unsigned long long,unsigned long long> p1;
      p1 = make_pair(i, jobs_[i]);
      Insert(p1);
      assigned_workers_[i] = i;
      start_times_[i] = next_free_time[i];
      next_free_time[i] += duration;
    }

    for (unsigned long long j = i; j < jobs_.size(); ++j) {
      unsigned long long duration = jobs_[i];
      unsigned long long next_worker = 0;
      /*
      for (unsigned long long j = 0; j < num_workers_; ++j) {
        if (next_free_time[j] < next_free_time[next_worker])
          next_worker = j;
      }
      */
      pair<unsigned long long,unsigned long long> thread = ExtractMin();
      next_worker = thread.first;
      start_times_[j] = thread.second;
      thread.second += jobs_[j];

      assigned_workers_[j] = next_worker;
      next_free_time[next_worker] += duration;

      Insert(thread);
    }
  }

 public:
  void Solve() {
    ReadData();
    AssignJobs();
    WriteResponse();
  }
};

int main() {
  std::ios_base::sync_with_stdio(false);
  JobQueue job_queue;
  job_queue.Solve();
  return 0;
}
