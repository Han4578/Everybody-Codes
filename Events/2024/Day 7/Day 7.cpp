#include <chrono>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;
using namespace chrono;


vector<int> read_opponent(string &line) {
	vector<int> actions;

	for (int i = 2; i < line.length(); ++i) {
		switch (line[i]) {
			case '+':
				actions.push_back(1);
				break;
			case '-':
				actions.push_back(-1);
				break;
			case '=':
				actions.push_back(0);
				break;
		}
	}

	return actions;
}

long get_essence(vector<int> &track, int full_length, vector<int> &plan) {
	long target = 10 * full_length;
	for (int i = 0; i < plan.size(); ++i) {
		for (int j = i; j < full_length; j += plan.size()) {
			if (track[j % track.size()] != 0) target += track[j % track.size()] * (full_length - j);
			else if (plan[i] != 0) target += (full_length - j) * plan[i];
		}
	}
	return target;
}

void P1() {
	string line = "";
	vector<pair<char, int>> rank;
	ifstream input("input.txt");

	while (getline(input, line)) {
		char device = line[0];
		int power = 10, total = 0;
		vector<int> actions = read_opponent(line);

		for (int i = 0; i < 10; ++i) {
			power += actions[i % actions.size()];
			if (power < 0) power = 0;

			total += power;
		}

		rank.push_back({ device, total });
	}

	sort(rank.begin(), rank.end(), [](pair<char, int> &a, pair<char, int> &b) {return a.second > b.second;});

	for (auto p : rank) {
		cout << p.first;
	}
}

void P2() {
	ifstream track_f("track.txt");
	ifstream input("p2.txt");
	vector<string> track_s;
	vector<int> track;
	string line = "";
	vector<pair<char, int>> rank;


	while (getline(track_f, line)) track_s.push_back(line);

	int dx = 1, dy = 0, x = 1, y = 0;
	while (x + y >= 0) {
		switch (track_s[y][x]) {
			case '+':
				track.push_back(1);
				break;
			case '-':
				track.push_back(-1);
				break;
			case 'S':
			case '=':
				track.push_back(0);
				break;

		}

		if (x + dx >= line.length() || y + dy >= (int)track_s.size() || x + dx < 0) {
			swap(dx, dy);
			dx *= -1;
		}

		x += dx;
		y += dy;
	}

	while (getline(input, line)) {
		char device = line[0];
		vector<int> actions = read_opponent(line);

		int total = get_essence(track, 10 * track.size(), actions);

		rank.push_back({ device, total });
	}

	sort(rank.begin(), rank.end(), [](pair<char, int> &a, pair<char, int> &b) {return a.second > b.second;});

	for (auto p : rank) {
		cout << p.first;
	}
}

void P3() {
	string line = "";
	ifstream trackf("p3_track.txt");
	vector<string> track_s;
	vector<int> track;
	int width = 0;

	while (getline(trackf, line)) {
		track_s.push_back(line);
		width = max(width, (int)line.length());
	}

	for (string &s : track_s) s += string(width - s.length(), ' ');

	pair<int, int> last_point = { 0, 0 }, current_point = { 1, 0 };
	int ci = 0, height = track_s.size();

	while (current_point.first > 0 || current_point.second > 0) {
		auto &[x, y] = current_point;
		switch (track_s[y][x]) {
			case '+':
				track.push_back(1);
				break;
			case '-':
				track.push_back(-1);
				break;
			case '=':
				track.push_back(0);
				break;

		}

		bool b = false;
		for (int dx : {-1, 0, 1}) {
			for (int dy : {-1, 0, 1}) {
				if (abs(dx) + abs(dy) != 1) continue;
				if (!(x + dx == last_point.first && y + dy == last_point.second) && x + dx < width && x + dx >= 0 && y + dy >= 0 && y + dy < height && track_s[y + dy][x + dx] != ' ') {
					last_point = current_point;
					x += dx;
					y += dy;
					b = true;
					break;
				}
			}
			if (b) break;
		}

	}

	track.push_back(0);

	int full_length = track.size();

	while (full_length % 11 != 0) full_length += track.size();

	vector< pair<string, long> > last = { {"", full_length * 10} }, current;
	const unordered_map<char, int> limit = { {'+', 5}, {'-', 3}, {'=', 3} };

	for (int i = 0; i < 11; ++i) {
		for (char c : {'+', '-', '='}) {
			for (auto &[plan, total] : last) {
				if (count(plan.begin(), plan.end(), c) >= limit.at(c)) continue;
				long val = 0;

				for (int j = i; j < full_length; j += 11) {
					if (track[j % track.size()] != 0) val += track[j % track.size()] * (full_length - j);
					else if (c != '=') val += (full_length - j) * ((c == '+') ? 1 : -1);
				}

				current.push_back({ plan + c, total + val });
			}
		}
		last = move(current);
	}

	ifstream opponent_f("p3 opponent.txt");
	string opponent_s = "";
	getline(opponent_f, opponent_s);
	vector<int> opponent = read_opponent(opponent_s);
	long target = get_essence(track, full_length, opponent);
	int total_plans = 0;

	for (auto &p : last) if (p.second > target) ++total_plans;
	
	cout << total_plans;
}

int main() {
	auto start = high_resolution_clock::now();
	P1();
	cout << '\n';
	P2();
	cout << '\n';
	P3();
	auto end = high_resolution_clock::now();
	auto duration = duration_cast<microseconds>(end - start);
	cout << '\n' << (float) duration.count() / 1000 << " ms";
	return 0;
}
