#pragma once
// Tiny test helper: CHECK(actual, expected) prints PASS/FAIL, SUMMARY() prints totals.
#include <algorithm>
#include <iostream>
#include <queue>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

inline int g_pass = 0, g_fail = 0;

template <typename T> string show(const T& v) { ostringstream o; o << v; return o.str(); }
inline string show(const string& s) { return "\"" + s + "\""; }
inline string show(bool b) { return b ? "true" : "false"; }
template <typename T> string show(const vector<T>& v) {
    string s = "[";
    for (size_t i = 0; i < v.size(); ++i) s += (i ? "," : "") + show(v[i]);
    return s + "]";
}

#define CHECK(actual, expected) do {                                        \
    auto _a = (actual); auto _e = (expected);                               \
    if (_a == _e) { ++g_pass; cout << "  PASS  line " << __LINE__ << "\n"; } \
    else { ++g_fail; cout << "  FAIL  line " << __LINE__                    \
        << "  got " << show(_a) << "  expected " << show(_e) << "\n"; }     \
} while (0)

#define SUMMARY() do {                                                      \
    cout << "\n" << g_pass << " passed, " << g_fail << " failed"           \
         << (g_fail == 0 ? "  ✔ all good\n" : "\n");                        \
    return g_fail == 0 ? 0 : 1;                                             \
} while (0)

// Linked list helpers
struct ListNode { int val; ListNode* next; ListNode(int x, ListNode* n = nullptr) : val(x), next(n) {} };
inline ListNode* makeList(const vector<int>& v) {
    ListNode* head = nullptr;
    for (int i = (int)v.size() - 1; i >= 0; --i) head = new ListNode(v[i], head);
    return head;
}
inline vector<int> toVec(ListNode* h) { vector<int> r; for (; h; h = h->next) r.push_back(h->val); return r; }
