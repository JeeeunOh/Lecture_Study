/*
* tn.h - token type(HW2)
*
* Programmer - team2
*
* date - 4/27/2021
*
*/

enum tnumber {
	TEOF, TONECMT, TMULCMT, TSTARCMT, TIDENT, TDECIMAL, TFIXED, TCONST, TELSE, TIF, TINT, TRETURN, TVOID, TWHILE, TPLUS, TMINUS, TSTAR, TSLASH, TMOD, TASSIGN, TADDASSIGN, TSUBASSIGN, TMULASSIGN, TDIVASSIGN, TMODASSGIN, TNOT, TAND, TOR, TEQUAL, TNOTEQU, TLESS, TOVER, TLESSE, TOVERE, TINC, TDEC, TOSBRA, TCSBRA, TCOMMA, TOMBRA, TCMBRA, TOLBRA, TCLBRA, TSEMI, TBLANK, TTAB, TNEWLINE, TILLSYM, TILLIDENT,
	TLONG, TOVERFLOW
};