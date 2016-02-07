# This file was automatically created by FeynRules $Revision: 302 $
# Mathematica version: 7.0 for Mac OS X x86 (64-bit) (November 11, 2008)
# Date: Tue 31 Aug 2010 16:54:46


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_21})

V_2 = Vertex(name = 'V_2',
             particles = [ P.G, P.G, P.G ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_3 = Vertex(name = 'V_3',
             particles = [ P.G, P.G, P.G, P.G ],
             color = [ 'f(2,3,\'a1\')*f(\'a1\',1,4)', 'f(2,4,\'a1\')*f(\'a1\',1,3)', 'f(3,4,\'a1\')*f(\'a1\',1,2)' ],
             lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
             couplings = {(1,1):C.GC_6,(2,0):C.GC_6,(0,2):C.GC_6})

V_4 = Vertex(name = 'V_4',
             particles = [ P.A, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_16})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVSS1 ],
             couplings = {(0,0):C.GC_10})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__plus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVS1 ],
             couplings = {(0,0):C.GC_22})

V_7 = Vertex(name = 'V_7',
             particles = [ P.A, P.A, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_18})

V_8 = Vertex(name = 'V_8',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_7})

V_9 = Vertex(name = 'V_9',
             particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_8})

V_10 = Vertex(name = 'V_10',
              particles = [ P.A, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_17})

V_11 = Vertex(name = 'V_11',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_20})

V_12 = Vertex(name = 'V_12',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_23})

V_13 = Vertex(name = 'V_13',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV2 ],
              couplings = {(0,0):C.GC_9})

V_14 = Vertex(name = 'V_14',
              particles = [ P.d__tilde__, P.d, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_15 = Vertex(name = 'V_15',
              particles = [ P.s__tilde__, P.s, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_16 = Vertex(name = 'V_16',
              particles = [ P.b__tilde__, P.b, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_17 = Vertex(name = 'V_17',
              particles = [ P.e__plus__, P.e__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_18 = Vertex(name = 'V_18',
              particles = [ P.m__plus__, P.m__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_19 = Vertex(name = 'V_19',
              particles = [ P.tt__plus__, P.tt__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_20 = Vertex(name = 'V_20',
              particles = [ P.u__tilde__, P.u, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_21 = Vertex(name = 'V_21',
              particles = [ P.c__tilde__, P.c, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_22 = Vertex(name = 'V_22',
              particles = [ P.t__tilde__, P.t, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_23 = Vertex(name = 'V_23',
              particles = [ P.d__tilde__, P.d, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_24 = Vertex(name = 'V_24',
              particles = [ P.s__tilde__, P.s, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_25 = Vertex(name = 'V_25',
              particles = [ P.b__tilde__, P.b, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_26 = Vertex(name = 'V_26',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_24})

V_27 = Vertex(name = 'V_27',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_14})

V_28 = Vertex(name = 'V_28',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_14})

V_29 = Vertex(name = 'V_29',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_14})

V_30 = Vertex(name = 'V_30',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_31 = Vertex(name = 'V_31',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_32 = Vertex(name = 'V_32',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_33 = Vertex(name = 'V_33',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_34 = Vertex(name = 'V_34',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_35 = Vertex(name = 'V_35',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_36 = Vertex(name = 'V_36',
              particles = [ P.u__tilde__, P.u, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_37 = Vertex(name = 'V_37',
              particles = [ P.c__tilde__, P.c, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_38 = Vertex(name = 'V_38',
              particles = [ P.t__tilde__, P.t, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_5})

V_39 = Vertex(name = 'V_39',
              particles = [ P.tt__plus__, P.tt__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_26})

V_40 = Vertex(name = 'V_40',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_25})

V_41 = Vertex(name = 'V_41',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_15})

V_42 = Vertex(name = 'V_42',
              particles = [ P.m__plus__, P.m__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_15})

V_43 = Vertex(name = 'V_43',
              particles = [ P.tt__plus__, P.tt__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_15})

V_44 = Vertex(name = 'V_44',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_45 = Vertex(name = 'V_45',
              particles = [ P.m__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_46 = Vertex(name = 'V_46',
              particles = [ P.tt__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_47 = Vertex(name = 'V_47',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_48 = Vertex(name = 'V_48',
              particles = [ P.vm__tilde__, P.m__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_49 = Vertex(name = 'V_49',
              particles = [ P.vt__tilde__, P.tt__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_50 = Vertex(name = 'V_50',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_13,(0,1):C.GC_14})

V_51 = Vertex(name = 'V_51',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_13,(0,1):C.GC_14})

V_52 = Vertex(name = 'V_52',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_13,(0,1):C.GC_14})

V_53 = Vertex(name = 'V_53',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_19})

V_54 = Vertex(name = 'V_54',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_19})

V_55 = Vertex(name = 'V_55',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_19})

#For gg>8g, uu~>8g and uu>uu6g

V_56 = Vertex(name = 'V_56',
             particles = [ P.g21, P.g32, P.g13 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_57 = Vertex(name = 'V_57',
             particles = [ P.g21, P.g42, P.g14 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_58 = Vertex(name = 'V_58',
             particles = [ P.g21, P.g52, P.g15 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_59 = Vertex(name = 'V_59',
             particles = [ P.g21, P.g62, P.g16 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_60 = Vertex(name = 'V_60',
             particles = [ P.g21, P.g72, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_61 = Vertex(name = 'V_61',
             particles = [ P.g21, P.g82, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_62 = Vertex(name = 'V_62',
             particles = [ P.g31, P.g43, P.g14 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_63 = Vertex(name = 'V_63',
             particles = [ P.g41, P.g54, P.g15 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_64 = Vertex(name = 'V_64',
             particles = [ P.g51, P.g65, P.g16 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_65 = Vertex(name = 'V_65',
             particles = [ P.g61, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_66 = Vertex(name = 'V_66',
             particles = [ P.g71, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_67 = Vertex(name = 'V_67',
             particles = [ P.g32, P.g43, P.g24 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_68 = Vertex(name = 'V_68',
             particles = [ P.g32, P.g53, P.g25 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_69 = Vertex(name = 'V_69',
             particles = [ P.g32, P.g63, P.g26 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_70 = Vertex(name = 'V_70',
             particles = [ P.g32, P.g73, P.g27 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_71 = Vertex(name = 'V_71',
             particles = [ P.g32, P.g83, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_72 = Vertex(name = 'V_72',
             particles = [ P.g42, P.g54, P.g25 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_73 = Vertex(name = 'V_73',
             particles = [ P.g52, P.g65, P.g26 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_74 = Vertex(name = 'V_74',
             particles = [ P.g62, P.g76, P.g27 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_75 = Vertex(name = 'V_75',
             particles = [ P.g72, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_76 = Vertex(name = 'V_76',
             particles = [ P.g43, P.g54, P.g35 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_77 = Vertex(name = 'V_77',
             particles = [ P.g43, P.g64, P.g36 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_78 = Vertex(name = 'V_78',
             particles = [ P.g43, P.g74, P.g37 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_79 = Vertex(name = 'V_79',
             particles = [ P.g43, P.g84, P.g38 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_80 = Vertex(name = 'V_80',
             particles = [ P.g53, P.g65, P.g36 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_81 = Vertex(name = 'V_81',
             particles = [ P.g63, P.g76, P.g37 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_82 = Vertex(name = 'V_82',
             particles = [ P.g73, P.g87, P.g38 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_83 = Vertex(name = 'V_83',
             particles = [ P.g54, P.g65, P.g46 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_84 = Vertex(name = 'V_84',
             particles = [ P.g54, P.g75, P.g47 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_85 = Vertex(name = 'V_85',
             particles = [ P.g54, P.g85, P.g48 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_86 = Vertex(name = 'V_86',
             particles = [ P.g64, P.g76, P.g47 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_87 = Vertex(name = 'V_87',
             particles = [ P.g74, P.g87, P.g48 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_88 = Vertex(name = 'V_88',
             particles = [ P.g65, P.g76, P.g57 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_89 = Vertex(name = 'V_89',
             particles = [ P.g65, P.g86, P.g58 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_90 = Vertex(name = 'V_90',
             particles = [ P.g75, P.g87, P.g58 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_91 = Vertex(name = 'V_91',
             particles = [ P.g76, P.g87, P.g68 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

V_92 = Vertex(name = 'V_92',
             particles = [ P.g87, P.g98, P.g79 ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_4})

# 4-point

V_93 = Vertex(name = 'V_93',
             particles = [ P.g21, P.g32, P.g43, P.g14 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_94 = Vertex(name = 'V_94',
             particles = [ P.g21, P.g32, P.g53, P.g15 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_95 = Vertex(name = 'V_95',
             particles = [ P.g21, P.g32, P.g63, P.g16 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_96 = Vertex(name = 'V_96',
             particles = [ P.g21, P.g32, P.g73, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_97 = Vertex(name = 'V_97',
             particles = [ P.g21, P.g32, P.g83, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_98 = Vertex(name = 'V_98',
             particles = [ P.g21, P.g42, P.g54, P.g15 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_99 = Vertex(name = 'V_99',
             particles = [ P.g21, P.g52, P.g65, P.g16 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_100 = Vertex(name = 'V_100',
             particles = [ P.g21, P.g62, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_101 = Vertex(name = 'V_101',
             particles = [ P.g21, P.g72, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_102 = Vertex(name = 'V_102',
             particles = [ P.g31, P.g43, P.g54, P.g15 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_103 = Vertex(name = 'V_103',
             particles = [ P.g41, P.g54, P.g65, P.g16 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_104 = Vertex(name = 'V_104',
             particles = [ P.g51, P.g65, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_105 = Vertex(name = 'V_105',
             particles = [ P.g61, P.g76, P.g87, P.g18],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_106 = Vertex(name = 'V_106',
             particles = [ P.g32, P.g43, P.g54, P.g25 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_107 = Vertex(name = 'V_107',
             particles = [ P.g32, P.g43, P.g64, P.g26 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_108 = Vertex(name = 'V_108',
             particles = [ P.g32, P.g43, P.g74, P.g27 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_109 = Vertex(name = 'V_109',
             particles = [ P.g32, P.g43, P.g84, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_110 = Vertex(name = 'V_110',
             particles = [ P.g32, P.g53, P.g65, P.g26 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_111 = Vertex(name = 'V_111',
             particles = [ P.g32, P.g63, P.g76, P.g27 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_112 = Vertex(name = 'V_112',
             particles = [ P.g32, P.g73, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_113 = Vertex(name = 'V_113',
             particles = [ P.g42, P.g54, P.g65, P.g26 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_114 = Vertex(name = 'V_114',
             particles = [ P.g52, P.g65, P.g76, P.g27 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_115 = Vertex(name = 'V_115',
             particles = [ P.g62, P.g76, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_116 = Vertex(name = 'V_116',
             particles = [ P.g43, P.g54, P.g65, P.g36 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_117 = Vertex(name = 'V_117',
             particles = [ P.g43, P.g54, P.g75, P.g37 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_118 = Vertex(name = 'V_118',
             particles = [ P.g43, P.g54, P.g85, P.g38 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_119 = Vertex(name = 'V_119',
             particles = [ P.g43, P.g64, P.g76, P.g37 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_120 = Vertex(name = 'V_120',
             particles = [ P.g43, P.g74, P.g87, P.g38 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_121 = Vertex(name = 'V_121',
             particles = [ P.g53, P.g65, P.g76, P.g37 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_122 = Vertex(name = 'V_122',
             particles = [ P.g63, P.g76, P.g87, P.g38 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_123 = Vertex(name = 'V_123',
             particles = [ P.g54, P.g65, P.g76, P.g47 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_124 = Vertex(name = 'V_124',
             particles = [ P.g54, P.g65, P.g86, P.g48 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_125 = Vertex(name = 'V_125',
             particles = [ P.g54, P.g75, P.g87, P.g48 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_126 = Vertex(name = 'V_126',
             particles = [ P.g64, P.g76, P.g87, P.g48 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_127 = Vertex(name = 'V_127',
             particles = [ P.g65, P.g76, P.g87, P.g58 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

V_128 = Vertex(name = 'V_128',
             particles = [ P.g76, P.g87, P.g98, P.g69 ],
             color = [ '1' ],
             lorentz = [ L.GLUON4 ],
             couplings = {(0,0):C.G2})

# 5-point

V_129 = Vertex(name = 'V129',
             particles = [ P.g21, P.g32, P.g43, P.g54, P.g15 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_130 = Vertex(name = 'V130',
             particles = [ P.g21, P.g32, P.g43, P.g64, P.g16 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_131 = Vertex(name = 'V131',
             particles = [ P.g21, P.g32, P.g43, P.g74, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_132 = Vertex(name = 'V132',
             particles = [ P.g21, P.g32, P.g43, P.g84, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_133 = Vertex(name = 'V133',
             particles = [ P.g21, P.g32, P.g53, P.g65, P.g16 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_134 = Vertex(name = 'V134',
             particles = [ P.g21, P.g32, P.g63, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_135 = Vertex(name = 'V135',
             particles = [ P.g21, P.g32, P.g73, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_136 = Vertex(name = 'V136',
             particles = [ P.g21, P.g42, P.g54, P.g65, P.g16 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_137 = Vertex(name = 'V137',
             particles = [ P.g21, P.g52, P.g65, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_138 = Vertex(name = 'V138',
             particles = [ P.g21, P.g62, P.g76, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_139 = Vertex(name = 'V139',
             particles = [ P.g31, P.g43, P.g54, P.g65, P.g16 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_140 = Vertex(name = 'V140',
             particles = [ P.g41, P.g54, P.g65, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_141 = Vertex(name = 'V141',
             particles = [ P.g51, P.g65, P.g76, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_142 = Vertex(name = 'V142',
             particles = [ P.g32, P.g43, P.g54, P.g65, P.g26 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_143 = Vertex(name = 'V143',
             particles = [ P.g32, P.g43, P.g54, P.g75, P.g27 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_144 = Vertex(name = 'V144',
             particles = [ P.g32, P.g43, P.g54, P.g85, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_145 = Vertex(name = 'V145',
             particles = [ P.g32, P.g43, P.g64, P.g76, P.g27 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_146 = Vertex(name = 'V146',
             particles = [ P.g32, P.g43, P.g74, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_147 = Vertex(name = 'V147',
             particles = [ P.g32, P.g53, P.g65, P.g76, P.g27 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_148 = Vertex(name = 'V148',
             particles = [ P.g32, P.g63, P.g76, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_149 = Vertex(name = 'V149',
             particles = [ P.g42, P.g54, P.g65, P.g76, P.g27 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_150 = Vertex(name = 'V150',
             particles = [ P.g52, P.g65, P.g76, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_151 = Vertex(name = 'V151',
             particles = [ P.g43, P.g54, P.g65, P.g76, P.g37 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_152 = Vertex(name = 'V152',
             particles = [ P.g43, P.g54, P.g65, P.g86, P.g38 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_153 = Vertex(name = 'V153',
             particles = [ P.g43, P.g54, P.g75, P.g87, P.g38 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_154 = Vertex(name = 'V154',
             particles = [ P.g43, P.g64, P.g76, P.g87, P.g38 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_155 = Vertex(name = 'V155',
             particles = [ P.g53, P.g65, P.g76, P.g87, P.g38 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_156 = Vertex(name = 'V156',
             particles = [ P.g54, P.g65, P.g76, P.g87, P.g48 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

V_157 = Vertex(name = 'V157',
             particles = [ P.g65, P.g76, P.g87, P.g98, P.g59 ],
             color = [ '1' ],
             lorentz = [ L.GLUON5 ],
             couplings = {(0,0):C.G2})

# 6-point

V_158 = Vertex(name = 'V158',
             particles = [ P.g21, P.g32, P.g43, P.g54, P.g65, P.g16 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_159 = Vertex(name = 'V159',
             particles = [ P.g21, P.g32, P.g43, P.g54, P.g75, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_160 = Vertex(name = 'V160',
             particles = [ P.g21, P.g32, P.g43, P.g54, P.g85, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_161 = Vertex(name = 'V161',
             particles = [ P.g21, P.g32, P.g43, P.g64, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_162 = Vertex(name = 'V162',
             particles = [ P.g21, P.g32, P.g43, P.g74, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_163 = Vertex(name = 'V163',
             particles = [ P.g21, P.g32, P.g53, P.g65, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_164 = Vertex(name = 'V164',
             particles = [ P.g21, P.g32, P.g63, P.g76, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_165 = Vertex(name = 'V165',
             particles = [ P.g21, P.g42, P.g54, P.g65, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_166 = Vertex(name = 'V166',
             particles = [ P.g21, P.g52, P.g65, P.g76, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_167 = Vertex(name = 'V167',
             particles = [ P.g31, P.g43, P.g54, P.g65, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_168 = Vertex(name = 'V168',
             particles = [ P.g41, P.g54, P.g65, P.g76, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_169 = Vertex(name = 'V169',
             particles = [ P.g32, P.g43, P.g54, P.g65, P.g76, P.g27 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_170 = Vertex(name = 'V170',
             particles = [ P.g32, P.g43, P.g54, P.g65, P.g86, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_171 = Vertex(name = 'V171',
             particles = [ P.g32, P.g43, P.g54, P.g75, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_172 = Vertex(name = 'V172',
             particles = [ P.g32, P.g43, P.g64, P.g76, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_173 = Vertex(name = 'V173',
             particles = [ P.g32, P.g53, P.g65, P.g76, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_174 = Vertex(name = 'V174',
             particles = [ P.g42, P.g54, P.g65, P.g76, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_175 = Vertex(name = 'V175',
             particles = [ P.g43, P.g54, P.g65, P.g76, P.g87, P.g38 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

V_176 = Vertex(name = 'V176',
             particles = [ P.g54, P.g65, P.g76, P.g87, P.g98, P.g49 ],
             color = [ '1' ],
             lorentz = [ L.GLUON6 ],
             couplings = {(0,0):C.G2})

# 7-point

V_177 = Vertex(name = 'V177',
             particles = [ P.g21, P.g32, P.g43, P.g54, P.g65, P.g76, P.g17 ],
             color = [ '1' ],
             lorentz = [ L.GLUON7 ],
             couplings = {(0,0):C.G2})

V_178 = Vertex(name = 'V178',
             particles = [ P.g21, P.g32, P.g43, P.g54, P.g65, P.g86, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON7 ],
             couplings = {(0,0):C.G2})

V_179 = Vertex(name = 'V179',
             particles = [ P.g21, P.g32, P.g43, P.g54, P.g75, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON7 ],
             couplings = {(0,0):C.G2})

V_180 = Vertex(name = 'V180',
             particles = [ P.g21, P.g32, P.g43, P.g64, P.g76, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON7 ],
             couplings = {(0,0):C.G2})

V_181 = Vertex(name = 'V181',
             particles = [ P.g21, P.g32, P.g53, P.g65, P.g76, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON7 ],
             couplings = {(0,0):C.G2})

V_182 = Vertex(name = 'V182',
             particles = [ P.g21, P.g42, P.g54, P.g65, P.g76, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON7 ],
             couplings = {(0,0):C.G2})

V_183 = Vertex(name = 'V183',
             particles = [ P.g31, P.g43, P.g54, P.g65, P.g76, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON7 ],
             couplings = {(0,0):C.G2})

V_184 = Vertex(name = 'V184',
             particles = [ P.g32, P.g43, P.g54, P.g65, P.g76, P.g87, P.g28 ],
             color = [ '1' ],
             lorentz = [ L.GLUON7 ],
             couplings = {(0,0):C.G2})

V_185 = Vertex(name = 'V185',
             particles = [ P.g43, P.g54, P.g65, P.g76, P.g87, P.g98, P.g39 ],
             color = [ '1' ],
             lorentz = [ L.GLUON7 ],
             couplings = {(0,0):C.G2})

# 8-point

V_186 = Vertex(name = 'V186',
             particles = [ P.g21, P.g32, P.g43, P.g54, P.g65, P.g76, P.g87, P.g18 ],
             color = [ '1' ],
             lorentz = [ L.GLUON8 ],
             couplings = {(0,0):C.G2})

V_187 = Vertex(name = 'V187',
             particles = [ P.g32, P.g43, P.g54, P.g65, P.g76, P.g87, P.g98, P.g29 ],
             color = [ '1' ],
             lorentz = [ L.GLUON8 ],
             couplings = {(0,0):C.G2})

# 9-point

V_188 = Vertex(name = 'V188',
             particles = [ P.g21, P.g32, P.g43, P.g54, P.g65, P.g76, P.g87, P.g98, P.g19 ],
             color = [ '1' ],
             lorentz = [ L.GLUON9 ],
             couplings = {(0,0):C.G2})

# 10-point

V_189 = Vertex(name = 'V189',
             particles = [ P.g21, P.g32, P.g43, P.g54, P.g65, P.g76, P.g87, P.g98, P.ga9, P.g1a ],
             color = [ '1' ],
             lorentz = [ L.GLUON10 ],
             couplings = {(0,0):C.G2})

# qqg

V_201 = Vertex(name = 'V_201',
              particles = [ P.u3__tilde__, P.u1, P.g13 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_202 = Vertex(name = 'V_202',
              particles = [ P.u1__tilde__, P.u3, P.g13 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_203 = Vertex(name = 'V_203',
              particles = [ P.u4__tilde__, P.u1, P.g14 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_204 = Vertex(name = 'V_204',
              particles = [ P.u1__tilde__, P.u4, P.g14 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_205 = Vertex(name = 'V_205',
              particles = [ P.u5__tilde__, P.u1, P.g15 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_206 = Vertex(name = 'V_206',
              particles = [ P.u1__tilde__, P.u5, P.g15 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_207 = Vertex(name = 'V_207',
              particles = [ P.u6__tilde__, P.u1, P.g16 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_208 = Vertex(name = 'V_208',
              particles = [ P.u1__tilde__, P.u6, P.g16 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_209 = Vertex(name = 'V_209',
              particles = [ P.u7__tilde__, P.u1, P.g17 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_210 = Vertex(name = 'V_210',
              particles = [ P.u1__tilde__, P.u7, P.g17 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_211 = Vertex(name = 'V_211',
              particles = [ P.u8__tilde__, P.u1, P.g18 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_212 = Vertex(name = 'V_212',
              particles = [ P.u1__tilde__, P.u8, P.g18 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_213 = Vertex(name = 'V_213',
              particles = [ P.u9__tilde__, P.u1, P.g19 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_214 = Vertex(name = 'V_214',
              particles = [ P.u1__tilde__, P.u9, P.g19 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_215 = Vertex(name = 'V_215',
              particles = [ P.u1__tilde__, P.u2, P.g21 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_216 = Vertex(name = 'V_216',
              particles = [ P.u2__tilde__, P.u1, P.g21 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_217 = Vertex(name = 'V_217',
              particles = [ P.u4__tilde__, P.u2, P.g24 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_218 = Vertex(name = 'V_218',
              particles = [ P.u2__tilde__, P.u4, P.g24 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_219 = Vertex(name = 'V_219',
              particles = [ P.u5__tilde__, P.u2, P.g25 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_220 = Vertex(name = 'V_220',
              particles = [ P.u2__tilde__, P.u5, P.g25 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_221 = Vertex(name = 'V_221',
              particles = [ P.u6__tilde__, P.u2, P.g26 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_222 = Vertex(name = 'V_222',
              particles = [ P.u2__tilde__, P.u6, P.g26 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_223 = Vertex(name = 'V_223',
              particles = [ P.u7__tilde__, P.u2, P.g27 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_224 = Vertex(name = 'V_224',
              particles = [ P.u2__tilde__, P.u7, P.g27 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_225 = Vertex(name = 'V_225',
              particles = [ P.u8__tilde__, P.u2, P.g28 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_226 = Vertex(name = 'V_226',
              particles = [ P.u2__tilde__, P.u8, P.g28 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_227 = Vertex(name = 'V_227',
              particles = [ P.u9__tilde__, P.u2, P.g29 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_228 = Vertex(name = 'V_228',
              particles = [ P.u2__tilde__, P.u9, P.g29 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})


V_229 = Vertex(name = 'V_229',
              particles = [ P.u3__tilde__, P.u1, P.g31 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_230 = Vertex(name = 'V_230',
              particles = [ P.u2__tilde__, P.u3, P.g32 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_231 = Vertex(name = 'V_231',
              particles = [ P.u3__tilde__, P.u2, P.g32 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_232 = Vertex(name = 'V_232',
              particles = [ P.u5__tilde__, P.u3, P.g35 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_233 = Vertex(name = 'V_233',
              particles = [ P.u3__tilde__, P.u5, P.g35 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_234 = Vertex(name = 'V_234',
              particles = [ P.u6__tilde__, P.u3, P.g36 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_235 = Vertex(name = 'V_235',
              particles = [ P.u3__tilde__, P.u6, P.g36 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_236 = Vertex(name = 'V_236',
              particles = [ P.u7__tilde__, P.u3, P.g37 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_237 = Vertex(name = 'V_237',
              particles = [ P.u3__tilde__, P.u7, P.g37 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_238 = Vertex(name = 'V_238',
              particles = [ P.u8__tilde__, P.u3, P.g38 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_239 = Vertex(name = 'V_239',
              particles = [ P.u3__tilde__, P.u8, P.g38 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_240 = Vertex(name = 'V_240',
              particles = [ P.u9__tilde__, P.u3, P.g39 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_241 = Vertex(name = 'V_241',
              particles = [ P.u3__tilde__, P.u9, P.g39 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_242 = Vertex(name = 'V_242',
              particles = [ P.u4__tilde__, P.u1, P.g41 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_243 = Vertex(name = 'V_243',
              particles = [ P.u4__tilde__, P.u2, P.g42 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_244 = Vertex(name = 'V_244',
              particles = [ P.u3__tilde__, P.u4, P.g43 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_245 = Vertex(name = 'V_245',
              particles = [ P.u4__tilde__, P.u3, P.g43 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_246 = Vertex(name = 'V_246',
              particles = [ P.u6__tilde__, P.u4, P.g46 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_247 = Vertex(name = 'V_247',
              particles = [ P.u4__tilde__, P.u6, P.g46 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_248 = Vertex(name = 'V_248',
              particles = [ P.u7__tilde__, P.u4, P.g47 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_249 = Vertex(name = 'V_249',
              particles = [ P.u4__tilde__, P.u7, P.g47 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_251 = Vertex(name = 'V_251',
              particles = [ P.u8__tilde__, P.u4, P.g48 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_252 = Vertex(name = 'V_252',
              particles = [ P.u4__tilde__, P.u8, P.g48 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_253 = Vertex(name = 'V_253',
              particles = [ P.u9__tilde__, P.u4, P.g49 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_254 = Vertex(name = 'V_254',
              particles = [ P.u4__tilde__, P.u9, P.g49 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_255 = Vertex(name = 'V_255',
              particles = [ P.u5__tilde__, P.u1, P.g51 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_256 = Vertex(name = 'V_256',
              particles = [ P.u5__tilde__, P.u2, P.g52 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_257 = Vertex(name = 'V_257',
              particles = [ P.u5__tilde__, P.u3, P.g53 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_258 = Vertex(name = 'V_258',
              particles = [ P.u4__tilde__, P.u5, P.g54 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_259 = Vertex(name = 'V_259',
              particles = [ P.u5__tilde__, P.u4, P.g54 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_260 = Vertex(name = 'V_260',
              particles = [ P.u7__tilde__, P.u5, P.g57 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_261 = Vertex(name = 'V_261',
              particles = [ P.u5__tilde__, P.u7, P.g57 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_262 = Vertex(name = 'V_262',
              particles = [ P.u8__tilde__, P.u5, P.g58 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_263 = Vertex(name = 'V_263',
              particles = [ P.u5__tilde__, P.u8, P.g58 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_264 = Vertex(name = 'V_264',
              particles = [ P.u9__tilde__, P.u5, P.g59 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_265 = Vertex(name = 'V_265',
              particles = [ P.u5__tilde__, P.u9, P.g59 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_266 = Vertex(name = 'V_266',
              particles = [ P.u6__tilde__, P.u1, P.g61 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_267 = Vertex(name = 'V_267',
              particles = [ P.u6__tilde__, P.u2, P.g62 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_268 = Vertex(name = 'V_268',
              particles = [ P.u6__tilde__, P.u3, P.g63 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_269 = Vertex(name = 'V_269',
              particles = [ P.u6__tilde__, P.u4, P.g64 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_270 = Vertex(name = 'V_270',
              particles = [ P.u5__tilde__, P.u6, P.g65 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_271 = Vertex(name = 'V_271',
              particles = [ P.u6__tilde__, P.u5, P.g65 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_272 = Vertex(name = 'V_272',
              particles = [ P.u8__tilde__, P.u6, P.g68 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_273 = Vertex(name = 'V_273',
              particles = [ P.u6__tilde__, P.u8, P.g68 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_274 = Vertex(name = 'V_274',
              particles = [ P.u9__tilde__, P.u6, P.g69 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_275 = Vertex(name = 'V_275',
              particles = [ P.u6__tilde__, P.u9, P.g69 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_276 = Vertex(name = 'V_276',
              particles = [ P.u7__tilde__, P.u1, P.g71 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_277 = Vertex(name = 'V_277',
              particles = [ P.u7__tilde__, P.u2, P.g72 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_278 = Vertex(name = 'V_278',
              particles = [ P.u7__tilde__, P.u3, P.g73 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_279 = Vertex(name = 'V_279',
              particles = [ P.u7__tilde__, P.u4, P.g74 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_280 = Vertex(name = 'V_280',
              particles = [ P.u7__tilde__, P.u5, P.g75 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_281 = Vertex(name = 'V_281',
              particles = [ P.u6__tilde__, P.u7, P.g76 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_282 = Vertex(name = 'V_282',
              particles = [ P.u7__tilde__, P.u6, P.g76 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_283 = Vertex(name = 'V_283',
              particles = [ P.u9__tilde__, P.u7, P.g79 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_284 = Vertex(name = 'V_284',
              particles = [ P.u7__tilde__, P.u9, P.g79 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_285 = Vertex(name = 'V_285',
              particles = [ P.u8__tilde__, P.u1, P.g81 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_286 = Vertex(name = 'V_286',
              particles = [ P.u8__tilde__, P.u2, P.g82 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_287 = Vertex(name = 'V_287',
              particles = [ P.u8__tilde__, P.u3, P.g83 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_288 = Vertex(name = 'V_288',
              particles = [ P.u8__tilde__, P.u4, P.g84 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_289 = Vertex(name = 'V_289',
              particles = [ P.u8__tilde__, P.u5, P.g85 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_290 = Vertex(name = 'V_290',
              particles = [ P.u8__tilde__, P.u6, P.g86 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_291 = Vertex(name = 'V_291',
              particles = [ P.u7__tilde__, P.u8, P.g87 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_292 = Vertex(name = 'V_292',
              particles = [ P.u8__tilde__, P.u7, P.g87 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_293 = Vertex(name = 'V_293',
              particles = [ P.u9__tilde__, P.u1, P.g91 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_294 = Vertex(name = 'V_294',
              particles = [ P.u9__tilde__, P.u2, P.g92 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_295 = Vertex(name = 'V_295',
              particles = [ P.u9__tilde__, P.u3, P.g93 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_296 = Vertex(name = 'V_296',
              particles = [ P.u9__tilde__, P.u4, P.g94 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_297 = Vertex(name = 'V_297',
              particles = [ P.u9__tilde__, P.u5, P.g95 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_298 = Vertex(name = 'V_298',
              particles = [ P.u9__tilde__, P.u6, P.g96 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_299 = Vertex(name = 'V_299',
              particles = [ P.u9__tilde__, P.u7, P.g97 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_300 = Vertex(name = 'V_300',
              particles = [ P.u8__tilde__, P.u9, P.g98 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_301 = Vertex(name = 'V_301',
              particles = [ P.u9__tilde__, P.u8, P.g98 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG2})

V_401 = Vertex(name = 'V_401',
              particles = [ P.u1__tilde__, P.u1, P.g0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG0})

V_402 = Vertex(name = 'V_402',
              particles = [ P.u2__tilde__, P.u2, P.g0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG0})

V_403 = Vertex(name = 'V_403',
              particles = [ P.u3__tilde__, P.u3, P.g0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG0})

V_404 = Vertex(name = 'V_404',
              particles = [ P.u4__tilde__, P.u4, P.g0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG0})

V_405 = Vertex(name = 'V_405',
              particles = [ P.u5__tilde__, P.u5, P.g0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG0})

V_406 = Vertex(name = 'V_406',
              particles = [ P.u6__tilde__, P.u6, P.g0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG0})

V_407 = Vertex(name = 'V_407',
              particles = [ P.u7__tilde__, P.u7, P.g0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG0})

V_408 = Vertex(name = 'V_408',
              particles = [ P.u8__tilde__, P.u8, P.g0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG0})

V_409 = Vertex(name = 'V_409',
              particles = [ P.u9__tilde__, P.u9, P.g0 ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GG0})


