## Linear algebra
Linear algebrais the branch ofmathematicsconcerninglinear equationssuch as
linear mapssuch as
and their representations invector spacesand throughmatrices.[1][2][3]
Linear algebra is central to almost all areas of mathematics. For instance, linear algebra is fundamental in modern presentations ofgeometry, including for defining basic objects such aslines,planesandrotations. Also,functional analysis, a branch ofmathematical analysis, may be viewed as the application of linear algebra tofunction spaces.
Linear algebra is also used in most sciences and fields ofengineeringbecause it allowsmodelingmany natural phenomena, and computing efficiently with such models. Fornonlinear systems, which cannot be modeled with linear algebra, it is often used for dealing withfirst-order approximations, using the fact that thedifferentialof amultivariate functionat a point is the linear map that best approximates the function near that point.

## History
The procedure (using counting rods) for solving simultaneous linear equations now calledGaussian eliminationappears in the ancient Chinese mathematical textChapter Eight:Rectangular ArraysofThe Nine Chapters on the Mathematical Art. Its use is illustrated in eighteen problems, with two to five equations.[4]
Systems of linear equationsarose in Europe with the introduction in 1637 byRené Descartesofcoordinatesingeometry. In fact, in this new geometry, now calledCartesian geometry, lines and planes are represented by linear equations, and computing their intersections amounts to solving systems of linear equations.
The first systematic methods for solving linear systems useddeterminantsand were first considered byLeibnizin 1693. In 1750,Gabriel Cramerused them for giving explicit solutions of linear systems, now calledCramer's rule. Later,Gaussfurther described the method of elimination, which was initially listed as an advancement ingeodesy.[5]
In 1844Hermann Grassmannpublished his "Theory of Extension" which included foundational new topics of what is today called linear algebra. In 1848,James Joseph Sylvesterintroduced the termmatrix, which is Latin forwomb.
Linear algebra grew with ideas noted in thecomplex plane. For instance, two numberswandzinC{\displaystyle \mathbb {C} }have a differencew–z, and the line segmentswzand0(w−z)are of the same length and direction. The segments areequipollent. The four-dimensional systemH{\displaystyle \mathbb {H} }ofquaternionswas discovered byW.R. Hamiltonin 1843.[6]The termvectorwas introduced asv=xi+yj+zkrepresenting a point in space. The quaternion differencep–qalso produces a segment equipollent topq. Otherhypercomplex numbersystems also used the idea of a linear space with abasis.
Arthur Cayleyintroducedmatrix multiplicationand theinverse matrixin 1856, making possible thegeneral linear group. The mechanism ofgroup representationbecame available for describing complex and hypercomplex numbers. Crucially, Cayley used a single letter to denote a matrix, thus treating a matrix as an aggregate object. He also realized the connection between matrices and determinants and wrote "There would be many things to say about this theory of matrices which should, it seems to me, precede the theory of determinants".[5]
Benjamin Peircepublished hisLinear Associative Algebra(1872), and his sonCharles Sanders Peirceextended the work later.[7]
Thetelegraphrequired an explanatory system, and the 1873 publication byJames Clerk MaxwellofA Treatise on Electricity and Magnetisminstituted afield theoryof forces and requireddifferential geometryfor expression. Linear algebra is flat differential geometry and serves in tangent spaces tomanifolds. Electromagnetic symmetries of spacetime are expressed by theLorentz transformations, and much of the history of linear algebra is thehistory of Lorentz transformations.
The first modern and more precise definition of a vector space was introduced byPeanoin 1888;[5]by 1900, a theory of linear transformations of finite-dimensional vector spaces had emerged. Linear algebra took its modern form in the first half of the twentieth century when many ideas and methods of previous centuries were generalized asabstract algebra. The development of computers led to increased research in efficientalgorithmsfor Gaussian elimination and matrix decompositions, and linear algebra became an essential tool for modeling and simulations.[5]

## Vector spaces
Until the 19th century, linear algebra was introduced throughsystems of linear equationsandmatrices. In modern mathematics, the presentation throughvector spacesis generally preferred, since it is moresynthetic, more general (not limited to the finite-dimensional case), and conceptually simpler, although more abstract.
A vector space over afieldF(often the field of thereal numbersor of thecomplex numbers) is asetVequipped with twobinary operations.ElementsofVare calledvectors, and elements ofFare calledscalars. The first operation,vector addition, takes any two vectorsvandwand outputs a third vectorv+w. The second operation,scalar multiplication, takes any scalaraand any vectorvand outputs a newvectorav. The axioms that addition and scalar multiplication must satisfy are the following. (In the list below,u,vandware arbitrary elements ofV, andaandbare arbitrary scalars in the fieldF.)[8]
The first four axioms mean thatVis anabelian groupunder addition.
The elements of a specific vector space may have various natures; for example, they could betuples,sequences,functions,polynomials, ormatrices. Linear algebra is concerned with the properties of such objects that are common to all vector spaces.

## Linear maps
Linear mapsaremappingsbetween vector spaces that preserve the vector-space structure. Given two vector spacesVandWover a fieldF, a linear map (also called, in some contexts, linear transformation or linear mapping) is amap
that is compatible with addition and scalar multiplication, that is
for any vectorsu,vinVand scalarainF.
An equivalent condition is that
for any vectorsu,vinVand scalarsa,binF.
WhenV=Ware the same vector space, a linear mapT:V→Vis also known as alinear operatoronV.
Abijectivelinear map between two vector spaces (that is, every vector from the second space is associated with exactly one in the first) is anisomorphism. Because an isomorphism preserves linear structure, two isomorphic vector spaces are "essentially the same" from the linear algebra point of view, in the sense that they cannot be distinguished by using vector space properties. An essential question in linear algebra is testing whether a linear map is an isomorphism or not, and, if it is not an isomorphism, finding itsrange(or image) and the set of elements that are mapped to the zero vector, called thekernelof the map. All these questions can be solved by usingGaussian eliminationor some variant of thisalgorithm.

## Subspaces, span, and basis
The study of those subsets of vector spaces that are in themselves vector spaces under the induced operations is fundamental, similarly as for many mathematical structures. These subsets are calledlinear subspaces. More precisely, a linear subspace of a vector spaceVover a fieldFis asubsetWofVsuch thatu+vandauare inW, for everyu,vinW, and everyainF. (These conditions suffice for implying thatWis a vector space.)
For example, given a linear mapT:V→W, theimageT(V)ofV, and theinverse imageT−1(0)of0(calledkernelor null space), are linear subspaces ofWandV, respectively.
Another important way of forming a subspace is to considerlinear combinationsof a setSof vectors: the set of all sums
wherev1,v2, ...,vkare inS, anda1,a2, ...,akare inFform a linear subspace called thespanofS. The span ofSis also the intersection of all linear subspaces containingS. In other words, it is the smallest (for the inclusion relation) linear subspace containingS.
A set of vectors islinearly independentif none is in the span of the others. Equivalently, a setSof vectors is linearly independent if the only way to express the zero vector as a linear combination of elements ofSis to take zero for every coefficientai.
A set of vectors that spans a vector space is called aspanning setorgenerating set. If a spanning setSislinearly dependent(that is not linearly independent), then some elementwofSis in the span of the other elements ofS, and the span would remain the same if one were to removewfromS. One may continue to remove elements ofSuntil getting alinearly independent spanning set. Such a linearly independent set that spans a vector spaceVis called abasisofV. The importance of bases lies in the fact that they are simultaneously minimal-generating sets and maximal independent sets. More precisely, ifSis a linearly independent set, andTis a spanning set such thatS⊆T, then there is a basisBsuch thatS⊆B⊆T.
Any two bases of a vector spaceVhave the samecardinality, which is called thedimensionofV; this is thedimension theorem for vector spaces. Moreover, two vector spaces over the same fieldFareisomorphicif and only if they have the same dimension.[9]
If any basis ofV(and therefore every basis) has a finite number of elements,Vis afinite-dimensional vector space. IfUis a subspace ofV, thendimU≤ dimV. In the case whereVis finite-dimensional, the equality of the dimensions impliesU=V.
IfU1andU2are subspaces ofV, then
whereU1+U2denotes the span ofU1∪U2.[10]

## Matrices
Matrices allow explicit manipulation of finite-dimensional vector spaces andlinear maps. Their theory is thus an essential part of linear algebra.
LetVbe a finite-dimensional vector space over a fieldF, and(v1,v2, ...,vm)be a basis ofV(thusmis the dimension ofV). By definition of a basis, the map
is abijectionfromFm, the set of thesequencesofmelements ofF, ontoV. This is anisomorphismof vector spaces, ifFmis equipped with its standard structure of vector space, where vector addition and scalar multiplication are done component by component.
This isomorphism allows representing a vector by itsinverse imageunder this isomorphism, that is by thecoordinate vector(a1, ...,am)or by thecolumn matrix
IfWis another finite dimensional vector space (possibly the same), with a basis(w1, ...,wn), a linear mapffromWtoVis well defined by its values on the basis elements, that is(f(w1), ...,f(wn)). Thus,fis well represented by the list of the corresponding column matrices. That is, if
forj= 1, ...,n, thenfis represented by the matrix
withmrows andncolumns.
Matrix multiplicationis defined in such a way that the product of two matrices is the matrix of thecompositionof the corresponding linear maps, and the product of a matrix and a column matrix is the column matrix representing the result of applying the represented linear map to the represented vector. It follows that the theory of finite-dimensional vector spaces and the theory of matrices are two different languages for expressing the same concepts.
Two matrices that encode the same linear transformation in different bases are calledsimilar. It can be proved that two matrices are similar if and only if one can transform one into the other byelementary row and column operations. For a matrix representing a linear map fromWtoV, the row operations correspond to change of bases inVand the column operations correspond to change of bases inW. Every matrix is similar to anidentity matrixpossibly bordered by zero rows and zero columns. In terms of vector spaces, this means that, for any linear map fromWtoV, there are bases such that a part of the basis ofWis mapped bijectively on a part of the basis ofV, and that the remaining basis elements ofW, if any, are mapped to zero.Gaussian eliminationis the basic algorithm for finding these elementary operations, and proving these results.

## Linear systems
A finite set of linear equations in a finite set of variables, for example,x1,x2, ...,xn, orx,y, ...,zis called asystem of linear equationsor alinear system.[11][12][13][14][15]
Systems of linear equations form a fundamental part of linear algebra. Historically, linear algebra and matrix theory have been developed for solving such systems. In the modern presentation of linear algebra through vector spaces and matrices, many problems may be interpreted in terms of linear systems.
For example, let
be a linear system.
To such a system, one may associate its matrix
and its right member vector
LetTbe the linear transformation associated with the matrixM. A solution of the system (S) is a vector
such that
that is an element of thepreimageofvbyT.
Let (S′) be the associatedhomogeneous system, where the right-hand sides of the equations are put to zero:
The solutions of (S′) are exactly the elements of thekernelofTor, equivalently,M.
TheGaussian-eliminationconsists of performingelementary row operationson theaugmented matrix
for putting it inreduced row echelon form. These row operations do not change the set of solutions of the system of equations. In the example, the reduced echelon form is
showing that the system (S) has the unique solution
More generally, a system ofm{\displaystyle m}linear equations inn{\displaystyle n}variables can be written asAx=b{\displaystyle A\mathbf {x} =\mathbf {b} }where
A=(aij)m×n{\displaystyle A=(a_{ij})_{m\times n}}
x=[x1⋮xn]{\displaystyle \mathbf {x} ={\begin{bmatrix}x_{1}\\\vdots \\x_{n}\end{bmatrix}}}
b=[b1⋮bm]{\displaystyle \mathbf {b} ={\begin{bmatrix}b_{1}\\\vdots \\b_{m}\end{bmatrix}}}
Ifm=n{\displaystyle m=n}and the matrixA{\displaystyle A}is invertible, then the system has the unique solutionx=A−1b{\displaystyle \mathbf {x} =A^{-1}\mathbf {b} }.
It follows from this matrix interpretation of linear systems that the same methods can be applied for solving linear systems and for many operations on matrices and linear transformations, which include the computation of theranks,kernels,matrix inverses.

## Endomorphisms and square matrices
A linearendomorphismis a linear map that maps a vector spaceVto itself. 
IfVhas a basis ofnelements, such an endomorphism is represented by a square matrix of sizen.
Concerning general linear maps, linear endomorphisms, and square matrices have some specific properties that make their study an important part of linear algebra, which is used in many parts of mathematics, includinggeometric transformations,coordinate changes,quadratic forms, and many other parts of mathematics.

## Determinant
Thedeterminantof a square matrixAis defined to be[16]
whereSnis thegroup of all permutationsofnelements,σis a permutation, and(−1)σtheparityof the permutation. A matrix isinvertibleif and only if the determinant is invertible (i.e., nonzero if the scalars belong to a field).
Cramer's ruleis aclosed-form expression, in terms of determinants, of the solution of asystem ofnlinear equations innunknowns. Cramer's rule is useful for reasoning about the solution, but, except forn= 2or3, it is rarely used for computing a solution, sinceGaussian eliminationis a faster algorithm.
Thedeterminant of an endomorphismis the determinant of the matrix representing the endomorphism in terms of some ordered basis. This definition makes sense since this determinant is independent of the choice of the basis.

## Eigenvalues and eigenvectors
Iffis a linear endomorphism of a vector spaceVover a fieldF, aneigenvectoroffis a nonzero vectorvofVsuch thatf(v) =avfor some scalarainF. This scalarais aneigenvalueoff.
If the dimension ofVis finite, and a basis has been chosen,fandvmay be represented, respectively, by a square matrixMand a column matrixz; the equation defining eigenvectors and eigenvalues becomes
Using theidentity matrixI, whose entries are all zero, except those of the main diagonal, which are equal to one, this may be rewritten
Aszis supposed to be nonzero, this means thatM–aIis asingular matrix, and thus that its determinantdet (M−aI)equals zero. The eigenvalues are thus therootsof thepolynomial
IfVis of dimensionn, this is amonic polynomialof degreen, called thecharacteristic polynomialof the matrix (or of the endomorphism), and there are, at most,neigenvalues.
If a basis exists that consists only of eigenvectors, the matrix offon this basis has a very simple structure: it is adiagonal matrixsuch that the entries on themain diagonalare eigenvalues, and the other entries are zero. In this case, the endomorphism and the matrix are said to bediagonalizable. More generally, an endomorphism and a matrix are also said diagonalizable, if they become diagonalizable afterextendingthe field of scalars. In this extended sense, if the characteristic polynomial issquare-free, then the matrix is diagonalizable.
Asymmetric matrixis always diagonalizable. There are non-diagonalizable matrices, the simplest being
(it cannot be diagonalizable since its square is thezero matrix, and the square of a nonzero diagonal matrix is never zero).
When an endomorphism is not diagonalizable, there are bases on which it has a simple form, although not as simple as the diagonal form. TheFrobenius normal formdoes not need to extend the field of scalars and makes the characteristic polynomial immediately readable on the matrix. TheJordan normal formrequires to extension of the field of scalar for containing all eigenvalues and differs from the diagonal form only by some entries that are just above the main diagonal and are equal to 1.

## Duality
Alinear formis a linear map from a vector spaceVover a fieldFto the field of scalarsF, viewed as a vector space over itself. Equipped bypointwiseaddition and multiplication by a scalar, the linear forms form a vector space, called thedual spaceofV, and usually denotedV*[17]orV′.[18][19]
Ifv1, ...,vnis a basis ofV(this implies thatVis finite-dimensional), then one can define, fori= 1, ...,n, a linear mapvi*such thatvi*(vi) = 1andvi*(vj) = 0ifj≠i. These linear maps form a basis ofV*, called thedual basisofv1, ...,vn. (IfVis not finite-dimensional, thevi*may be defined similarly; they are linearly independent, but do not form a basis.)
ForvinV, the map
is a linear form onV*. This defines thecanonical linear mapfromVinto(V*)*, the dual ofV*, called thedouble dualorbidualofV. This canonical map is anisomorphismifVis finite-dimensional, and this allows identifyingVwith its bidual. (In the infinite-dimensional case, the canonical map is injective, but not surjective.)
There is thus a complete symmetry between a finite-dimensional vector space and its dual. This motivates the frequent use, in this context, of thebra–ket notation
for denotingf(x).

## Dual map
Let
be a linear map. For every linear formhonW, thecomposite functionh∘fis a linear form onV. This defines a linear map
between the dual spaces, which is called thedualor thetransposeoff.
IfVandWare finite-dimensional, andMis the matrix offin terms of some ordered bases, then the matrix off*over the dual bases is thetransposeMTofM, obtained by exchanging rows and columns.
If elements of vector spaces and their duals are represented by column vectors, this duality may be expressed inbra–ket notationby
To highlight this symmetry, the two members of this equality are sometimes written

## Inner-product spaces
Besides these basic concepts, linear algebra also studies vector spaces with additional structure, such as aninner product. The inner product is an example of abilinear form, and it gives the vector space a geometric structure by allowing for the definition of length and angles. Formally, aninner productis a map.
that satisfies the following threeaxiomsfor all vectorsu,v,winVand all scalarsainF:[20][21]
We can define the length of a vectorvinVby
and we can prove theCauchy–Schwarz inequality:
In particular, the quantity
and so we can call this quantity the cosine of the angle between the two vectors.
Two vectors are orthogonal if⟨u,v⟩ = 0. An orthonormal basis is a basis where all basis vectors have length 1 and are orthogonal to each other. Given any finite-dimensional vector space, an orthonormal basis could be found by theGram–Schmidtprocedure. Orthonormal bases are particularly easy to deal with, since ifv=a1v1+ ⋯ +anvn, then
The inner product facilitates the construction of many useful concepts. For instance, given a transformT, we can define itsHermitian conjugateT*as the linear transform satisfying
IfTsatisfiesTT*=T*T, we callTnormal. It turns out that normal matrices are precisely the matrices that have an orthonormal system of eigenvectors that spanV.

## Relationship with geometry
There is a strong relationship between linear algebra andgeometry, which started with the introduction byRené Descartes, in 1637, ofCartesian coordinates. In this new (at that time) geometry, now calledCartesian geometry, points are represented byCartesian coordinates, which are sequences of three real numbers (in the case of the usualthree-dimensional space). The basic objects of geometry, which arelinesandplanesare represented by linear equations. Thus, computing intersections of lines and planes amounts to solving systems of linear equations. This was one of the main motivations for developing linear algebra.
Mostgeometric transformation, such astranslations,rotations,reflections,rigid motions,isometries, andprojectionstransform lines into lines. It follows that they can be defined, specified, and studied in terms of linear maps. This is also the case ofhomographiesandMöbius transformationswhen considered as transformations of aprojective space.
Until the end of the 19th century, geometric spaces were defined byaxiomsrelating points, lines, and planes (synthetic geometry). Around this date, it appeared that one may also define geometric spaces by constructions involving vector spaces (see, for example,Projective spaceandAffine space). It has been shown that the two approaches are essentially equivalent.[22]In classical geometry, the involved vector spaces are vector spaces over the reals, but the constructions may be extended to vector spaces over any field, allowing considering geometry over arbitrary fields, includingfinite fields.
Presently, most textbooks introduce geometric spaces from linear algebra, and geometry is often presented, at the elementary level, as a subfield of linear algebra.

## Usage and applications
Linear algebra is used in almost all areas of mathematics, thus making it relevant in almost all scientific domains that use mathematics. These applications may be divided into several wide categories.

## Functional analysis
Functional analysisstudiesfunction spaces. These are vector spaces with additional structure, such asHilbert spaces. Linear algebra is thus a fundamental part of functional analysis and its applications, which include, in particular,quantum mechanics(wave functions) andFourier analysis(orthogonal basis).

## Scientific computation
Nearly allscientific computationsinvolve linear algebra. Consequently, linear algebra algorithms have been highly optimized.BLASandLAPACKare the best known implementations. For improving efficiency, some of them configure the algorithms automatically, at run time, to adapt them to the specificities of the computer (cachesize, number of availablecores, ...).
Since the 1960s there have been processors with specialized instructions[23]for optimizing the operations of linear algebra, optional array processors[24]under the control of a conventional processor, supercomputers[25][26][27]designed for array processing and conventional processors augmented[28]with vector registers.
Some contemporaryprocessors, typicallygraphics processing units(GPU), are designed with a matrix structure, for optimizing the operations of linear algebra.[29]

## Geometry of ambient space
Themodelingofambient spaceis based ongeometry. Sciences concerned with this space use geometry widely. This is the case withmechanicsandrobotics, for describingrigid body dynamics;geodesyfor describingEarth shape;perspectivity,computer vision, andcomputer graphics, for describing the relationship between a scene and its plane representation; and many other scientific domains.
In all these applications,synthetic geometryis often used for general descriptions and a qualitative approach, but for the study of explicit situations, one must compute withcoordinates. This requires the heavy use of linear algebra.

## Study of complex systems
Most physical phenomena are modeled bypartial differential equations. To solve them, one usually decomposes the space in which the solutions are searched into small, mutually interactingcells. Forlinear systemsthis interaction involveslinear functions. Fornonlinear systems, this interaction is often approximated by linear functions.[b]This is called a linear model or first-order approximation. Linear models are frequently used for complex nonlinear real-world systems because they makeparametrizationmore manageable.[30]In both cases, very large matrices are generally involved.Weather forecasting(or more specifically,parametrization for atmospheric modeling) is a typical example of a real-world application, where the whole Earthatmosphereis divided into cells of, say, 100 km of width and 100 km of height.

## Fluid mechanics, fluid dynamics, and thermal energy systems
[31][32][33]
Linear algebra, a branch of mathematics dealing withvector spacesandlinear mappingsbetween these spaces, plays a critical role in various engineering disciplines, includingfluid mechanics,fluid dynamics, andthermal energysystems. Its application in these fields is multifaceted and indispensable for solving complex problems.
Influid mechanics, linear algebra is integral to understanding and solving problems related to the behavior of fluids. It assists in the modeling and simulation of fluid flow, providing essential tools for the analysis offluid dynamicsproblems. For instance, linear algebraic techniques are used to solve systems ofdifferential equationsthat describe fluid motion. These equations, often complex andnon-linear, can be linearized using linear algebra methods, allowing for simpler solutions and analyses.
In the field of fluid dynamics, linear algebra finds its application incomputational fluid dynamics(CFD), a branch that usesnumerical analysisanddata structuresto solve and analyze problems involving fluid flows. CFD relies heavily on linear algebra for the computation of fluid flow andheat transferin various applications. For example, theNavier–Stokes equations, fundamental influid dynamics, are often solved using techniques derived from linear algebra. This includes the use ofmatricesandvectorsto represent and manipulate fluid flow fields.
Furthermore, linear algebra plays a crucial role inthermal energysystems, particularly inpower systemsanalysis. It is used to model and optimize the generation,transmission, anddistributionof electric power. Linear algebraic concepts such as matrix operations andeigenvalueproblems are employed to enhance the efficiency, reliability, and economic performance ofpower systems. The application of linear algebra in this context is vital for the design and operation of modernpower systems, includingrenewable energysources andsmart grids.
Overall, the application of linear algebra influid mechanics,fluid dynamics, andthermal energysystems is an example of the profound interconnection betweenmathematicsandengineering. It provides engineers with the necessary tools to model, analyze, and solve complex problems in these domains, leading to advancements in technology and industry.

## Extensions and generalizations
This section presents several related topics that do not appear generally in elementary textbooks on linear algebra but are commonly considered, in advanced mathematics, as parts of linear algebra.

## Module theory
The existence of multiplicative inverses in fields is not involved in the axioms defining a vector space. One may thus replace the field of scalars by aringR, and this gives the structure called amoduleoverR, orR-module.
The concepts of linear independence, span, basis, and linear maps (also calledmodule homomorphisms) are defined for modules exactly as for vector spaces, with the essential difference that, ifRis not a field, there are modules that do not have any basis. The modules that have a basis are thefree modules, and those that are spanned by a finite set are thefinitely generated modules. Module homomorphisms between finitely generated free modules may be represented by matrices. The theory of matrices over a ring is similar to that of matrices over a field, except thatdeterminantsexist only if the ring iscommutative, and that a square matrix over a commutative ring isinvertibleonly if its determinant has amultiplicative inversein the ring.
Vector spaces are completely characterized by their dimension (up to an isomorphism). In general, there is not such a complete classification for modules, even if one restricts oneself to finitely generated modules. However, every module is acokernelof a homomorphism of free modules.
Modules over the integers can be identified withabelian groups, since the multiplication by an integer may be identified as a repeated addition. Most of the theory of abelian groups may be extended to modules over aprincipal ideal domain. In particular, over a principal ideal domain, every submodule of a free module is free, and thefundamental theorem of finitely generated abelian groupsmay be extended straightforwardly to finitely generated modules over a principal ring.
There are many rings for which there are algorithms for solving linear equations and systems of linear equations. However, these algorithms have generally acomputational complexitythat is much higher than similar algorithms over a field. For more details, seeLinear equation over a ring.

## Multilinear algebra and tensors
Inmultilinear algebra, one considers multivariable linear transformations, that is, mappings that are linear in each of several different variables. This line of inquiry naturally leads to the idea of thedual space, the vector spaceV*consisting of linear mapsf:V→FwhereFis the field of scalars. Multilinear mapsT:Vn→Fcan be described viatensor productsof elements ofV*.
If, in addition to vector addition and scalar multiplication, there is a bilinear vector productV×V→V, the vector space is called analgebra; for instance, associative algebras are algebras with an associate vector product (like the algebra of square matrices, or the algebra of polynomials).

## Topological vector spaces
Vector spaces that are not finite-dimensional often require additional structure to be tractable. Anormed vector spaceis a vector space along with a function called anorm, which measures the "size" of elements. The norm induces ametric, which measures the distance between elements, and induces atopology, which allows for a definition of continuous maps. The metric also allows for a definition oflimitsandcompleteness– a normed vector space that is complete is known as aBanach space. A complete metric space along with the additional structure of aninner product(a conjugate symmetricsesquilinear form) is known as aHilbert space, which is in some sense a particularly well-behaved Banach space.Functional analysisapplies the methods of linear algebra alongside those ofmathematical analysisto study various function spaces; the central objects of study in functional analysis areLpspaces, which are Banach spaces, and especially theL2space of square-integrable functions, which is the only Hilbert space among them. Functional analysis is of particular importance to quantum mechanics, the theory of partial differential equations, digital signal processing, and electrical engineering. It also provides the foundation and theoretical framework that underlies the Fourier transform and related methods.