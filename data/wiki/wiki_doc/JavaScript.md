## JavaScript
JavaScript(JS)[a]is aprogramming languageand core technology ofthe Web, alongsideHTMLandCSS. It was created byBrendan Eichin 1995.[6]As of 2025, the overwhelming majority ofwebsites(98.9%) uses JavaScript forclientsidewebpagebehavior.[10]
Web browsershave a dedicatedJavaScript enginethat executes the clientcode. These engines are also utilized in someserversand a variety ofapps. The most popularruntime systemfor non-browser usage isNode.js.[11]
JavaScript is ahigh-level, oftenjust-in-time–compiledlanguage that conforms to theECMAScriptstandard.[12]It hasdynamic typing,prototype-basedobject-orientation, andfirst-class functions. It ismulti-paradigm, supportingevent-driven,functional, andimperativeprogramming styles. It hasapplication programming interfaces(APIs) for working with text, dates,regular expressions, standarddata structures, and theDocument Object Model(DOM).
The ECMAScript standard does not include anyinput/output(I/O), such asnetworking,storage, orgraphicsfacilities. In practice, the web browser or other runtime system provides JavaScript APIs for I/O.
AlthoughJavaand JavaScript are similar in name andsyntax, the two languages are distinct and differ greatly in design.

## Creation at Netscape
The first popularweb browserwith agraphical user interface,Mosaic, was released in 1993. The lead developers of Mosaic then founded theNetscapecorporation, which released a more polished browser,Netscape Navigator, in 1994. This quickly became the most-used.[13]
During these formative years of the Web,web pagescould only be static, lacking the capability for dynamic behavior after the page was loaded in the browser. There was a desire in the flourishing web development scene to remove this limitation, so in 1995, Netscape decided to add aprogramming languageto Navigator. They pursued two routes to achieve this: collaborating withSun Microsystemsto embed theJavalanguage, while also hiringBrendan Eichto embed theSchemelanguage.[6]
The goal was a "language for the masses",[14]"to help nonprogrammers create dynamic, interactiveWeb sites".[15]Netscape management soon decided that the best option was for Eich to devise a new language, with syntax similar to Java and less like Scheme or other extantscripting languages.[5][6]Although the new language and itsinterpreterimplementation were called LiveScript when first shipped as part of a Navigatorbetain September 1995, the name was changed to JavaScript for the official release in December.[6][1][16][17]
The choice of theJavaScriptname has caused confusion, implying that it is directly related to Java. At the time, thedot-com boomhad begun and Java was a popular new language, so Eich considered the JavaScript name a marketing ploy by Netscape.[14]

## Adoption by Microsoft
MicrosoftdebutedInternet Explorerin 1995, leading to abrowser warwith Netscape. On the JavaScript front, Microsoft created its owninterpretercalledJScript.[18]
Microsoft first released JScript in 1996, alongside initial support forCSSand extensions toHTML. Each of theseimplementationswas noticeably different from their counterparts inNetscape Navigator.[19][20]These differences made it difficult for developers to make their websites work well in both browsers, leading to widespread use of "best viewed in Netscape" and "best viewed in Internet Explorer" logos for several years.[19][21]

## The rise of JScript
Brendan Eichlater said of this period: "It's still kind of asidekicklanguage. It's considered slow or annoying. People dopop-upsor those scrolling messages in the oldstatus barat the bottom of your oldbrowser."[14]
In November 1996,Netscapesubmitted JavaScript toEcma International, as the starting point for a standard specification that all browser vendors could conform to. This led to the official release of the firstECMAScriptlanguage specification in June 1997.
The standards process continued for a few years, with the release of ECMAScript 2 in June 1998 and ECMAScript 3 in December 1999. Work on ECMAScript 4 began in 2000.[18]
However, the effort to fully standardize the language was undermined by Microsoft gaining an increasingly dominant position in the browser market. By the early 2000s,Internet Explorer's market share reached 95%.[22]This meant thatJScriptbecame the de facto standard forclient-side scriptingon the Web.
Microsoft initially participated in the standards process and implemented some proposals in its JScript language, but eventually it stopped collaborating on ECMA work. Thus ECMAScript 4 was mothballed.

## Growth and standardization
During the period ofInternet Explorerdominance in the early 2000s, client-side scripting was stagnant. This started to change in 2004, when the successor of Netscape,Mozilla, released theFirefoxbrowser. Firefox was well received by many, taking significant market share from Internet Explorer.[23]
In 2005, Mozilla joined ECMA International, and work started on theECMAScript for XML(E4X) standard. This led to Mozilla working jointly withMacromedia(later acquired byAdobe Systems), who were implementing E4X in their ActionScript 3 language, which was based on an ECMAScript 4 draft. The goal became standardizing ActionScript 3 as the new ECMAScript 4. To this end, Adobe Systems released theTamarinimplementation as anopen sourceproject. However, Tamarin and ActionScript 3 were too different from established client-side scripting, and without cooperation from Microsoft, ECMAScript 4 never reached fruition.
Meanwhile, very important developments were occurring in open-source communities not affiliated with ECMA work. In 2005,Jesse James Garrettreleased a white paper in which he coined the termAjaxand described a set of technologies, of which JavaScript was the backbone, to createweb applicationswhere data can be loaded in the background, avoiding the need for full page reloads. This sparked a renaissance period of JavaScript, spearheaded by open-source libraries and the communities that formed around them. Many new libraries were created, includingjQuery,Prototype,Dojo Toolkit, andMooTools.
Googledebuted itsChromebrowser in 2008, with theV8JavaScript engine that was faster than its competition.[24][25]The key innovation wasjust-in-time compilation(JIT),[26]so other browser vendors needed to overhaul their engines for JIT.[27]
In July 2008, these disparate parties came together for a conference inOslo. This led to the eventual agreement in early 2009 to combine all relevant work and drive the language forward. The result was the ECMAScript 5 standard, released in December 2009.

## Reaching maturity
Ambitious work on the language continued for several years, culminating in an extensive collection of additions and refinements being formalized with the publication ofECMAScript 6in 2015.[28]
The creation ofNode.jsin 2009 byRyan Dahlsparked a significant increase in the usage of JavaScript outside of web browsers. Node combines theV8engine, anevent loop, andI/OAPIs, thereby providing a stand-alone JavaScript runtime system.[29][30]As of 2018, Node had been used by millions of developers,[31]andnpmhad the most modules of anypackage managerin the world.[32]
The ECMAScript draft specification is currently maintained openly onGitHub,[33]and editions are produced via regular annual snapshots.[33]Potential revisions to the language are vetted through a comprehensive proposal process.[34][35]Now, instead of edition numbers, developers check the status of upcoming features individually.[33]
The current JavaScript ecosystem has manylibrariesandframeworks, established programming practices, and substantial usage of JavaScript outside of web browsers.[17]Plus, with the rise ofsingle-page applicationsand other JavaScript-heavy websites, severaltranspilershave been created to aid the development process.[36]

## Trademark
"JavaScript" is atrademarkofOracle Corporationin the United States.[37][38]The trademark was originally issued toSun Microsystemson 6 May 1997, and was transferred to Oracle when they acquired Sun in 2009.[39][40]
A letter was circulated in September 2024, spearheaded byRyan Dahl, calling on Oracle to free the JavaScript trademark.[41]Brendan Eich, the original creator of JavaScript, was among the over 14,000 signatories who supported the initiative.

## Website client-side usage
JavaScript is the dominantclient-sidescripting languageof the Web, with 99% of allwebsitesusing it for this purpose.[10]Scripts are embedded in or included fromHTMLdocuments and interact with theDOM.
All majorweb browsershave a built-inJavaScript enginethat executes thecodeon the user's device.

## Libraries and frameworks
Over 80% of websites use a third-party JavaScriptlibraryorweb frameworkas part of their client-side scripting.[42]
jQueryis by far the most-used.[42]Other notable ones includeAngular,Bootstrap,Lodash,Modernizr,React,Underscore, andVue.[42]Multiple options can be used in conjunction, such as jQuery and Bootstrap.[43]
However, the term "Vanilla JS" was coined for websites not using any libraries or frameworks at all, instead relying entirely on standard JavaScript functionality.[44]

## Other usage
The use of JavaScript has expanded beyond itsweb browserroots.JavaScript enginesare now embedded in a variety of other software systems, both forserver-sidewebsite deployments and non-browserapplications.
Initial attempts at promoting server-side JavaScript usage wereNetscape Enterprise ServerandMicrosoft'sInternet Information Services,[45][46]but they were small niches.[47]Server-side usage eventually started to grow in the late 2000s, with the creation ofNode.jsandother approaches.[47]
Electron,Cordova,React Native, and otherapplication frameworkshave been used to create many applications with behavior implemented in JavaScript. Other non-browser applications includeAdobe Acrobatsupport for scriptingPDFdocuments[48]andGNOME Shellextensions written in JavaScript.[49]
Oracleused to provideNashorn, a JavaScript interpreter, as part of theirJava Development Kit (JDK)API library along withjjsa command line interpreter as of JDK version 8.  It was removed in JDK 15. As a replacement Oracle offered GraalJS which can also be used with theOpenJDKwhich allows one to create and reference Java objects in JavaScript code and add runtime scripting in JavaScript to applications written in Java.[50][51][52][53]
JavaScript has been used in someembedded systems, usually by leveraging Node.js.[54][55][56]

## JavaScript engine
The firstenginesfor JavaScript were mereinterpretersof thesource code, but all relevant modern engines usejust-in-time compilationfor improved performance.[57]JavaScript engines are typically developed byweb browservendors, and every major browser has one. In a browser, the JavaScript engine runs in concert with therendering enginevia theDocument Object ModelandWeb IDLbindings.[58]However, the use of JavaScript engines is not limited to browsers; for example, theV8 engineis a core component of theNode.jsruntime system.[59]They are also calledECMAScriptengines, after the official name of the specification. With the advent ofWebAssembly, some engines can also execute this code in the samesandboxas regular JavaScript code.[60][59]

## Runtime system
A JavaScript engine must be embedded within aruntime system(such as aweb browseror a standalone system) to enable scripts to interact with the broader environment. The runtime system includes the necessary APIs forinput/outputoperations, such asnetworking,storage, andgraphics, and provides the ability to import scripts.
JavaScript is a single-threadedlanguage. The runtime processesmessagesfrom aqueueone at a time, and it calls afunctionassociated with each new message, creating acall stackframe with the function'sargumentsandlocal variables. The call stack shrinks and grows based on the function's needs. When the call stack is empty upon function completion, JavaScript proceeds to the next message in the queue. This is called theevent loop, described as "run to completion" because each message is fully processed before the next message is considered. However, the language'sconcurrency modeldescribes the event loop asnon-blocking: program I/O is performed usingeventsandcallback functions. This means, for example, that JavaScript can process a mouse click while waiting for a database query to return information.[61]
The notable standalone runtimes areNode.js,Deno, andBun.

## Features
The following features are common to all conforming ECMAScript implementations unless explicitly specified otherwise. The number of cited reserved words including keywords is 50–60 and varies depending on the implementation.

## Imperative and structured
JavaScript supports much of thestructured programmingsyntax fromC(e.g.,ifstatements,whileloops,switchstatements,do whileloops, etc.). One partial exception isscoping: originally JavaScript only hadfunction scopingwithvar;block scopingwas added in ECMAScript 2015 with the keywordsletandconst. Like C, JavaScript makes a distinction betweenexpressionsandstatements. One syntactic difference from C isautomatic semicolon insertion, which allow semicolons (which terminate statements) to be omitted.[62]

## Weakly typed
JavaScript isweakly typed, which means certain types are implicitly cast depending on the operation used.[63]
Values are cast to strings as follows:[63]
Values are cast to numbers by casting to strings and then casting the strings to numbers. These processes can be modified by definingtoStringandvalueOffunctions on theprototypefor string and number casting respectively.
JavaScript has received criticism for the way it implements these conversions as the complexity of the rules can be mistaken for inconsistency.[65][63]For example, when adding a number to a string, the number will be cast to a string before performing concatenation, but when subtracting a number from a string, the string is cast to a number before performing subtraction.
Often also mentioned is{} + []resulting in0(number). This is misleading: the{}is interpreted as an empty code block instead of an empty object, and the empty array is cast to a number by the remaining unary+operator. If the expression is wrapped in parentheses -({} + [])– the curly brackets are interpreted as an empty object and the result of the expression is"[object Object]"as expected.[63]

## Typing
JavaScript isdynamically typedlike most otherscripting languages. Atypeis associated with avaluerather than an expression. For example, avariableinitially bound to a number may be reassigned to astring.[66]JavaScript supports various ways to test the type of objects, includingduck typing.[67]

## Run-time evaluation
JavaScript includes anevalfunction that can execute statements provided as strings at run-time.

## Object-orientation (prototype-based)
Prototypal inheritance in JavaScript is described byDouglas Crockfordas:
You make prototype objects, and then ... make new instances. Objects are mutable in JavaScript, so we can augment the new instances, giving them new fields and methods. These can then act as prototypes for even newer objects. We don't need classes to make lots of similar objects... Objects inherit from objects. What could be more object oriented than that?[68]
In JavaScript, anobjectis anassociative array, augmented with a prototype (see below); each key provides the name for an objectproperty, and there are two syntactical ways to specify such a name: dot notation (obj.x = 10) and bracket notation (obj["x"] = 10). A property may be added, rebound, or deleted at run-time. Mostpropertiesof an object (and any property that belongs to an object's prototype inheritance chain) can be enumerated using afor...inloop.

## Prototypes
JavaScript usesprototypeswhere many other object-oriented languages useclassesforinheritance,[69]but it's still possible to simulate most class-based features with the prototype system.[70]Additionally,ECMAScript version 6(released June 2015) introduced the keywordsclass,extendsandsuper, which serve as syntactic sugar to abstract the underlying prototypal inheritance system with a more conventional interface. Constructors are declared by specifying a method namedconstructor, and all classes are automatically subclasses of the base class Object, similarly to Java.
Though the underlying object mechanism is still based on prototypes, the newer syntax is similar to other object oriented languages. Private variables are declared by prefixing the field name with anumber sign(#), andpolymorphismis not directly supported, although it can be emulated by manually calling different functions depending on the number and type of arguments provided.[71]

## Functions as object constructors
Functions double as object constructors, along with their typical role. Prefixing a function call withnewwill create an instance of a prototype, inheriting properties and methods from the constructor (including properties from theObjectprototype).[72]ECMAScript 5 offers theObject.createmethod, allowing explicit creation of an instance without automatically inheriting from theObjectprototype (older environments can assign the prototype tonull).[73]The constructor'sprototypeproperty determines the object used for the new object's internal prototype. New methods can be added by modifying the prototype of the function used as a constructor.
JavaScript's built-in classes, such asArrayandObject, also have prototypes that can be modified. However, it's generally considered bad practice tomodify built-in objects, because third-party code may use or inherit methods and properties from these objects, and may not expect the prototype to be modified.[74]

## Functions as methods
Unlike in many object-oriented languages, in JavaScript there is no distinction between a function definition and amethoddefinition. Rather, the distinction occurs during function calling. When a function is called as a method of an object, the function's localthiskeyword is bound to that object for that invocation.

## Functional
JavaScriptfunctionsarefirst-class; a function is considered to be an object.[75]As such, a function may have properties and methods, such as.call()and.bind().[76]

## Lexical closure
Anestedfunction is a function defined within another function. It is created each time the outer function is invoked.
In addition, each nested function forms alexical closure: thelexical scopeof the outer function (including any constant, local variable, or argument value) becomes part of the internal state of each inner function object, even after execution of the outer function concludes.[77]

## Anonymous function
JavaScript also supportsanonymous functions.

## Delegative
JavaScript supports implicit and explicitdelegation.

## Functions as roles (Traits and Mixins)
JavaScript natively supports various function-based implementations ofRole[78]patterns likeTraits[79][80]andMixins.[81]Such a function defines additional behavior by at least one method bound to thethiskeyword within itsfunctionbody. A Role then has to be delegated explicitly viacallorapplyto objects that need to feature additional behavior that is not shared via the prototype chain.

## Object composition and inheritance
Whereas explicit function-based delegation does covercompositionin JavaScript, implicit delegation already happens every time the prototype chain is walked in order to, e.g., find a method that might be related to but is not directly owned by an object. Once the method is found it gets called within this object's context. Thusinheritancein JavaScript is covered by a delegation automatism that is bound to the prototype property of constructor functions.

## Zero-based numbering
JavaScript is azero-indexlanguage.

## Variadic functions
An indefinite number of parameters can be passed to a function. The function can access them throughformal parametersand also through the localargumentsobject.Variadic functionscan also be created by using thebindmethod.

## Array and object literals
Like in many scripting languages, arrays and objects (associative arraysin other languages) can each be created with a succinct shortcut syntax. In fact, theseliteralsform the basis of theJSONdata format.

## Regular expressions
JavaScript supportsregular expressionsfor text searches and manipulation.[72]: 139

## Promises
A built-in Promise object provides functionality for handling promises and associating handlers with an asynchronous action's eventual result. JavaScript supplies combinator methods, which allow developers to combine multiple JavaScript promises and do operations based on different scenarios. The methods introduced are: Promise.race, Promise.all, Promise.allSettled and Promise.any.

## Async/await
Async/await allows an asynchronous, non-blocking function to be structured in a way similar to an ordinary synchronous function. Asynchronous, non-blocking code can be written, with minimal overhead, structured similarly to traditional synchronous, blocking code.

## Vendor-specific extensions
Historically, someJavaScript enginessupported these non-standard features:

## Syntax
Variablesin JavaScript can be defined using either thevar,[83]let[84]orconst[85]keywords.  Variables defined without keywords will be defined at the global scope.
Arrow functions were first introduced in6th Edition – ECMAScript 2015. They shorten the syntax for writing functions in JavaScript. Arrow functions are anonymous, so a variable is needed to refer to them in order to invoke them after their creation, unless surrounded by parenthesis and executed immediately.
Here is an example of JavaScript syntax.
Note thecommentsin the examples above, all of which were preceded with twoforward slashes.
More examples can be found at theWikibooks page on JavaScript syntax examples.

## Security
JavaScript and theDOMprovide the potential for malicious authors to deliver scripts to run on a client computer via the Web. Browser authors minimize this risk using two restrictions. First, scripts run in asandboxin which they can only perform Web-related actions, not general-purpose programming tasks like creating files. Second, scripts are constrained by thesame-origin policy: scripts from one website do not have access to information such as usernames, passwords, or cookies sent to another site. Most JavaScript-related security bugs are breaches of either the same origin policy or the sandbox.
There are subsets of general JavaScript—ADsafe, Secure ECMAScript (SES)—that provide greater levels of security, especially on code created by third parties (such as advertisements).[86][87]Closure Toolkit is another project for safe embedding and isolation of third-party JavaScript and HTML.[88]
Content Security Policyis the main intended method of ensuring that only trusted code is executed on a Web page.

## Cross-site scripting
A common JavaScript-related security problem iscross-site scripting(XSS), a violation of thesame-origin policy. XSS vulnerabilities occur when an attacker can cause a target Website, such as an online banking website, to include a malicious script in the webpage presented to a victim. The script in this example can then access the banking application with the privileges of the victim, potentially disclosing secret information or transferring money without the victim's authorization. One important solution to XSS vulnerabilities isHTML sanitization.
Some browsers include partial protection againstreflectedXSS attacks, in which the attacker provides a URL including malicious script. However, even users of those browsers are vulnerable to other XSS attacks, such as those where the malicious code is stored in a database. Only correct design of Web applications on the server-side can fully prevent XSS.
XSS vulnerabilities can also occur because of implementation mistakes by browser authors.[89]

## Cross-site request forgery
Another cross-site vulnerability iscross-site request forgery(CSRF). In CSRF, code on an attacker's site tricks the victim's browser into taking actions the user did not intend at a target site (like transferring money at a bank). When target sites rely solely on cookies for request authentication, requests originating from code on the attacker's site can carry the same valid login credentials of the initiating user. In general, the solution to CSRF is to require an authentication value in a hidden form field, and not only in the cookies, to authenticate any request that might have lasting effects. Checking the HTTP Referrer header can also help.
"JavaScript hijacking" is a type of CSRF attack in which a<script>tag on an attacker's site exploits a page on the victim's site that returns private information such asJSONor JavaScript. Possible solutions include:

## Misplaced trust in the client
Developers of client-server applications must recognize that untrusted clients may be under the control of attackers. The author of an application should not assume that their JavaScript code will run as intended (or at all) because any secret embedded in the code could be extracted by a determined adversary. Some implications are:

## Misplaced trust in developers
Package management systems such asnpmand Bower are popular with JavaScript developers. Such systems allow a developer to easily manage their program's dependencies upon other developers' program libraries. Developers trust that the maintainers of the libraries will keep them secure and up to date, but that is not always the case. A vulnerability has emerged because of this blind trust. Relied-upon libraries can have new releases that cause bugs or vulnerabilities to appear in all programs that rely upon the libraries. Inversely, a library can go unpatched with known vulnerabilities out in the wild. In a study done looking over a sample of 133,000 websites, researchers found 37% of the websites included a library with at least one known vulnerability.[92]"The median lag between the oldest library version used on each website and the newest available version of that library is 1,177 days in ALEXA, and development of some libraries still in active use ceased years ago."[92]Another possibility is that the maintainer of a library may remove the library entirely. This occurred in March 2016 when Azer Koçulu removed his repository from npm. This caused tens of thousands of programs and websites depending upon his libraries to break.[93][94]

## Browser and plugin coding errors
JavaScript provides an interface to a wide range of browser capabilities, some of which may have flaws such asbuffer overflows. These flaws can allow attackers to write scripts that would run any code they wish on the user's system. This code is not by any means limited to another JavaScript application. For example, a buffer overrun exploit can allow an attacker to gain access to the operating system'sAPIwith superuser privileges.
These flaws have affected major browsers including Firefox,[95]Internet Explorer,[96]and Safari.[97]
Plugins, such as video players,Adobe Flash, and the wide range ofActiveXcontrols enabled by default in Microsoft Internet Explorer, may also have flaws exploitable via JavaScript (such flaws have been exploited in the past).[98][99]
In Windows Vista, Microsoft has attempted to contain the risks of bugs such as buffer overflows by running the Internet Explorer process with limited privileges.[100]Google Chromesimilarly confines its page renderers to their own "sandbox".

## Sandbox implementation errors
Web browsers are capable of running JavaScript outside the sandbox, with the privileges necessary to, for example, create or delete files. Such privileges are not intended to be granted to code from the Web.
Incorrectly granting privileges to JavaScript from the Web has played a role in vulnerabilities in both Internet Explorer[101]and Firefox.[102]In Windows XP Service Pack 2, Microsoft demoted JScript's privileges in Internet Explorer.[103]
Microsoft Windowsallows JavaScript source files on a computer's hard drive to be launched as general-purpose, non-sandboxed programs (see:Windows Script Host). This makes JavaScript (likeVBScript) a theoretically viable vector for aTrojan horse, although JavaScript Trojan horses are uncommon in practice.[104][failed verification]

## Hardware vulnerabilities
In 2015, a JavaScript-based proof-of-concept implementation of arowhammerattack was described in a paper by security researchers.[105][106][107][108]
In 2017, a JavaScript-based attack via browser was demonstrated that could bypassASLR. It is called "ASLR⊕Cache" or AnC.[109][110]
In 2018, the paper that announced theSpectreattacks against Speculative Execution in Intel and other processors included a JavaScript implementation.[111]

## Development tools
Important tools have evolved with the language.

## Java
A common misconception is that JavaScript is directly related toJava. Both indeed have a C-like syntax (the C language being their most immediate common ancestor language). They are also typicallysandboxed, and JavaScript was designed with Java's syntax and standard library in mind. In particular, all Java keywords were reserved in original JavaScript, JavaScript's standard library follows Java's naming conventions, and JavaScript'sMathandDateobjects are based on classes from Java 1.0.[114]
Both languages first appeared in 1995, but Java was developed byJames Goslingof Sun Microsystems and JavaScript byBrendan Eichof Netscape Communications.
The differences between the two languages are more prominent than their similarities. Java hasstatic typing, while JavaScript's typing isdynamic. Java is loaded fromcompiledbytecode, while JavaScript is loaded as human-readable source code. Java's objects areclass-based, while JavaScript's areprototype-based. Finally, Java did not support functional programming until Java 8, while JavaScript has done so from the beginning, being influenced byScheme.

## JSON
JSONis a data format derived from JavaScript; hence the name JavaScript Object Notation. It is a widely used format supported by many other programming languages.

## Transpilers
Many websites are JavaScript-heavy, sotranspilershave been created to convert code written in other languages, which can aid the development process.[36]
TypeScriptandCoffeeScriptare two notable languages that transpile to JavaScript.

## WebAssembly
WebAssemblyis a newer language with abytecodeformat designed to complement JavaScript, especially the performance-critical portions ofweb pagescripts. All of the majorJavaScript enginessupport WebAssembly,[115]which runs in the samesandboxas regular JavaScript code.
asm.jsis a subset of JavaScript that served as the forerunner of WebAssembly.[116]