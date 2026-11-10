#include <iostream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

void p1();
void p2();
void p3();

struct hash_pair {
	size_t operator()(const pair<int, int> &p) const {
		return p.first * 1000 + p.second;
	}
};

void count_horizontal_runes(string &line, unordered_set<pair<int, int>, hash_pair> &indexes, pair<const int, vector<string>> &p, int y);
void count_vertical_runes(string &line, unordered_set<pair<int, int>, hash_pair> &indexes, pair<const int, vector<string>> &p, int y);

int main() {
	p3();
	return 0;
}

void p1() {
	string words = "WORDS:LOR,LL,SI,OR,EN,T.,XC";
	string warray[] = { "LOR", "LL", "SI", "OR", "EN", "T.", "XC" };
	string input = "LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT, SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA.UT ENIM AD MINIM VENIAM, QUIS NOSTRUD EXERCITATION ULLAMCO LABORIS NISI UT ALIQUIP EX EA COMMODO CONSEQUAT.DUIS AUTE IRURE DOLOR IN REPREHENDERIT IN VOLUPTATE VELIT ESSE CILLUM DOLORE EU FUGIAT NULLA PARIATUR.EXCEPTEUR SINT OCCAECAT CUPIDATAT NON PROIDENT, SUNT IN CULPA QUI OFFICIA DESERUNT MOLLIT ANIM ID EST LABORUM.";
	string window = "";
	int i = 0;
	int count = 0;

	while (input.length() > 0) {
		for (string s : warray) {
			if (input.substr(0, s.length()) == s) {
				++count;
				break;
			}
		}
		input.erase(input.begin());
	}

	cout << count;
}

void p2() {
	ifstream input("p2.txt");

	string line = "";
	int count = 0;

	getline(input, line);
	unordered_map<int, vector<string>> words;
	string temp;
	int len = 0;
	for (int i = 6; i < line.length(); ++i) {
		if (line[i] == ',') {
			words[len].push_back(temp);
			reverse(temp.begin(), temp.end());
			words[len].push_back(temp);
			temp = "";
			len = 0;
		}
		else {
			temp += line[i];
			++len;
		}
	}
	words[len].push_back(temp);


	input.ignore();

	while (getline(input, line)) {
		unordered_set<pair<int, int>, hash_pair> indexes;
		for (auto &p : words) {
			count_horizontal_runes(line, indexes, p, 0);
		}
		count += indexes.size();
	}

	cout << count;
}

void p3() {
	ifstream input("p3.txt");

	string line = "";

	getline(input, line);
	unordered_map<int, vector<string>> words;
	string temp;
	int len = 0;
	for (int i = 6; i < line.length(); ++i) {
		if (line[i] == ',') {
			words[len].push_back(temp);
			reverse(temp.begin(), temp.end());
			words[len].push_back(temp);
			temp = "";
			len = 0;
		}
		else {
			temp += line[i];
			++len;
		}
	}
	words[len].push_back(temp);


	input.ignore();
	vector<string> map;

	while (getline(input, line)) map.push_back(line);

	unordered_set<pair<int, int>, hash_pair> indexes;
	for (auto &p : words) {
		int y = 0;
		for (string line : map) {
			count_horizontal_runes(line, indexes, p, y);
			++y;
		}
		for (int x = 0; x < line.length(); ++x) {
			string l = "";
			for (string s : map) l += s[x];
			count_vertical_runes(l, indexes, p, x);
		}
	}

	cout << indexes.size();
}

void count_horizontal_runes(string &line, unordered_set<pair<int, int>, hash_pair> &indexes, pair<const int, vector<string>> &p, int y) {
	string window = "";
	for (int i = -p.first + 1; i < 0; ++i) {
		window += line[i % line.length()];
	}

	for (int i = 0; i < line.length(); ++i) {
		window += line[i];
		if (window.length() > p.first) window.erase(window.begin());
		for (auto &s : p.second) {

			if (s == window) {
				for (int j = i - p.first; j < i; ++j) {
					int x = (j + 1) % line.length();
					indexes.insert(make_pair(x, y));
				}
				break;
			}
		}
	}
}

void count_vertical_runes(string &line, unordered_set<pair<int, int>, hash_pair> &indexes, pair<const int, vector<string>> &p, int x) {
	string window = "";
	for (int i = 0; i < p.first - 1; ++i) {
		window += line[i];
	}

	for (int i = p.first - 1; i < line.length(); ++i) {
		window += line[i];
		if (i >= p.first) window.erase(window.begin());
		for (auto &s : p.second) {

			if (s == window) {
				for (int j = i - p.first; j < i; ++j) indexes.insert(make_pair(x, j + 1));
				break;
			}
		}
	}
}