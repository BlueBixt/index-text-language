![ITL Logo](itl_logo_transparent.png)

# {ITL} - Index Text Language

<p>

![Version](https://img.shields.io/badge/Version-v1.4.0-3B82F6?style=for-the-badge)
![Color](https://img.shields.io/badge/Color-%233B82F6-3B82F6?style=for-the-badge)
![Org](https://img.shields.io/badge/Org-BlueBixt-3B82F6?style=for-the-badge)
![Status](https://img.shields.io/badge/PR-GitHub%20Linguist-yellow?style=for-the-badge)

</p>

**ITL is a pure Tools-based programming language created by BlueBixt.**

No operators like `==`, `+`, `=`. Everything is a Tool: `xxx{}`.

---

## ✨ Why ITL?

Other languages use symbols: `if (a == b) { }`
Other Language Have This Tools:
If{IsEqual{a,b}}
  Print{Equal}
EndIf{}


- **Pure:** Only `ToolName{}` syntax
- **Readable:** English-like Tools
- **Simple:** No symbols to memorize
- **Blue:** Signature color #3B82F6

---

## 📦 Installation

### From Source
```bash
git clone https://github.com/BlueBixt/index-text-language.git
cd index-text-language
```

---

### Requirements
- Any text editor (VS Code recommended)
- ITL Extension: .itl

---

### Core Tools I/O • Print{content} - Output text • Input{varName} - Get user input  Variables • Var{name: value} - Declare variable • List{name: [a,b,c]} - List • Dict{name: {k:v}} - Dictionary  Logic • If{condition} - Conditional • Else{} - Else branch • EndIf{} - End if • IsEqual{a,b} - Equality check • IsGreater{a,b} - Greater than  Loops • For{i From x To y} - For loop • EndFor{} - End loop • While{condition} - While loop • EndWhile{}  Functions • Func{name} - Define function • EndFunc{} - End function • Call{name} - Call function • Return{value} - Return value 

---


🎨 Syntax Highlighting
ITL highlighting is provided by:
• syntax/itl.tmLanguage.json - In this repo • vendor/grammars/ITL/itl.tmLanguage.json - For GitHub Linguist 
Color: Blue #3B82F6

To test locally in VS Code, copy grammar to .vscode/extensions.

---

Made with 💙 BlueBixt in PH
