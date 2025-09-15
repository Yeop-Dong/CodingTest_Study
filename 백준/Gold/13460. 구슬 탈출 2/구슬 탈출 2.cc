#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int, int>> DIR = { { -1,0 }, { 0,1 }, { 1,0 }, { 0,-1 } };

pair<int, int> pair_sum(pair<int, int> op1, pair<int, int> op2) {
	return make_pair(op1.first + op2.first, op1.second + op2.second);
}

void paint(vector<vector<char>> &board) {
	system("cls");
	for (auto line : board) {
		for (auto b : line) {
			cout << b;
		}
		cout << endl;
	}
}
int roll(vector<vector<char>> &board, pair<int, int> &r, pair<int, int> &b, pair<int, int> &o, int dir, int before) {
	bool r_upper = r.first < b.first;
	bool r_lefter = r.second < b.second;

	bool prior_r;
	switch (dir) {
	case 0: prior_r = r_upper; if (before == 2) return -1; break;
	case 1: prior_r = !r_lefter; if (before == 3) return -1; break;
	case 2: prior_r = !r_upper; if (before == 0) return -1; break;
	case 3: prior_r = r_lefter; if (before == 1) return -1; break;
	default: break;
	}
	pair<int, int> orig_r = r, orig_b = b;

	pair<int, int> save;
	if (prior_r) {
		board[r.first][r.second] = '.';
		do {
			save = r;
			r = pair_sum(r, DIR[dir]);
		} while (board[r.first][r.second] == '.');
		if (r != o) {
			r = save;
			board[r.first][r.second] = 'R';
		}
		//paint(board);
	}
	board[b.first][b.second] = '.';
	do {
		save = b;
		b = pair_sum(b, DIR[dir]);
	} while (board[b.first][b.second] == '.');
	if (b == o) return -1;
	
	b = save;
	board[b.first][b.second] = 'B';
	//paint(board);
	if (!prior_r) {
		board[r.first][r.second] = '.';
		do {
			save = r;
			r = pair_sum(r, DIR[dir]);
		} while (board[r.first][r.second] == '.');
		if (r != o) {
			r = save;
			board[r.first][r.second] = 'R';
		}
		//paint(board);
	}
	if (r == o) return 1;
	if (orig_r == r && orig_b == b) return -1;
	return 0;
}

int solution(vector<vector<char>> board, pair<int, int> r, pair<int, int> b, pair<int, int> o, int depth = 0, int before = -1) {
	if (depth == 11) return 11;
	vector<int> results;
	vector<vector<char>> save_board = board;
	pair<int, int> save_r = r, save_b = b, save_o = o;
	for (int i = 0; i < 4; i++) {
		int res = roll(board, r, b, o, i, before);
		//paint(board);

		if (res == 1) return depth + 1;
		else if (res == -1) results.push_back(11);
		else results.push_back(solution(board, r, b, o, depth + 1, i));
		
		//system("pause");
		board = save_board;
		r = save_r; b = save_b; o = save_o;
	}

	return *min_element(results.begin(), results.end());
}

int main() {

	
	int row, col;
	cin >> row >> col;

	vector<vector<char>> board(row, vector<char>(col));
	pair<int, int> r, b, o;

	for (int i = 0; i < row; i++) {
		getchar();
		for (int j = 0; j < col; j++) {
			cin >> board[i][j];
			switch (board[i][j]) {
			case 'R':
				r = { i, j };
				break;
			case 'B':
				b = { i, j };
				break;
			case 'O':
				o = { i, j };
				break;
			default:
				break;
			}
		}
	}

	int res = solution(board, r, b, o);
	printf("%d", res == 11 ? -1 : res);

	return 0;
}