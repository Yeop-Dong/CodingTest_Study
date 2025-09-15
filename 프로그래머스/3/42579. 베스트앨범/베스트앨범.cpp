#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <tuple>
#include <iostream>
using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
	vector<int> answer;
	vector<pair<string, int>> gencnt;
	vector<tuple<int, string, int>> song;

	for (auto i = 0; i < genres.size(); i++) {
		auto it = find_if(gencnt.begin(), gencnt.end(), [=](auto gc)->bool {
			return gc.first == genres[i];
		});
		if (it != gencnt.end()) it->second += plays[i];
		else gencnt.push_back(make_pair(genres[i], plays[i]));
		song.push_back(make_tuple(i, genres[i], plays[i]));
	}

	sort(gencnt.begin(), gencnt.end(), [=](auto a, auto b)->bool {
		return a.second > b.second;
	});
	sort(song.begin(), song.end(), [=](auto a, auto b)->bool {
		return get<2>(a) > get<2>(b);
	});
	
	for (auto g : gencnt) {
		auto it = find_if(song.begin(), song.end(), [=](auto s)->bool {
			return get<1>(s) == g.first;
		});
        if (it == song.end()) continue;
        answer.push_back(get<0>(*it));
		it = find_if(it+1, song.end(), [=](auto s)->bool {
			return get<1>(s) == g.first;
		});
        if (it == song.end()) continue;
        answer.push_back(get<0>(*it));
		
	}
	return answer;
}