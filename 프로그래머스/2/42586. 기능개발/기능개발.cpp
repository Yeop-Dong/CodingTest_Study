#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
	vector<int> answer;
	vector<int> req;

	for (int i = 0; i < progresses.size(); i++) {
		int r = ceil((100 - progresses[i]) / (double)speeds[i]);
		req.push_back(r);
	}

	for (auto r : req) {
		cout << r << " ";
	}

	while (!req.empty()) {
		int r = req[0];
		int cnt = 0;

		while (true) {
			auto end = find_if(req.begin(), req.end(), [=](int i)->bool {
				return i > r;
			});
			auto it = find_if(req.begin(), end, [=](int i)->bool {
				return i <= r;
			});
			if (it == end) break;
			req.erase(it);
			cnt++;
		}
		answer.push_back(cnt);
	}

	return answer;
}