import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import artcode_i, artcode_r

WWF_input = """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKo,.   .:dOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMKl.         .oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWx.             cXMMMMMMMMMMMMMMMMMMMMMWKkolloxKWMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMk.               oWMMMMMMMMMMMMMMMMMMWO;.      .,xXMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWo                ;XMMMMMMMMMMMMMMMMMNo.           ,OW
MMMMMMMMMMMMMMMMMMMMMMMMMMMk.             .;OWMMMMMMMMMMMMMMMMWd              '0
MMMMMMMMMMMMMWKO0NMMMMMMMMMWk.       .,odkXWMMMMMMMMMMMMMMMMMMWl               d
MMMMMMMMMMWXxldkXMMMMMMMMMNOc. .   .lOWMMMMMMMMMMMMMMMMMMMMMMMMXxc'           .k
MMMMMMMMWOc,c0WMMMMMMMMMNx,  .xK0kOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk:.       .xW
MMMMMMWO;.,OWMMMMMMMMMNx'   ,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;    .lKMM
MMMMMKc..lXMMMMMMMMMWO;    ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOxdOXMMMM
MMMWk' .dWMMMMMMMMMNd.    ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMWx.  oWMMMMMMMMMNo.    .OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MWx.  :XMMMMMMMMMWd.     lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MO.  .xMMMMMMMMMMO.     .kMMMMMMMMMMN0dllloONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
Nc   ,KMMMMMMMMMWc      ,KMMMMMMMMNx,.      :KMMMMMMMMMMMMN0OOKWMMMMMMMMMMMMWWMM
O.   :NMMMMMMMMM0'      ;XMMMMMMM0;          cNMMMMMMMMMNk,.  .,dXMMMMMMMMMMOdXM
o    :NMMMMMMMMMk.      '0MMMMMMK;           '0MMMMMMMMNo.       ,0MMMMMMMMMd'xM
:    ,KMMMMMMMMMx.      .xMMMMMMx.          .oXMMMMMMMMx.         ,KMMMMMMMWl cW
;    .kMMMMMMMMMx.       :XMMMMMO.         ;0WMMMMMMMMMK;         .xMMMMMMMK, ;X
;     cNMMMMMMMMx.        lNMMMMWx.      'dNMMMMMMMMMMMMK;        .xMMMMMMWl  '0
c     .xWMMMMMMMx.         cXMMMMWKdlclk0XMMMMMMMMMMMMMMM0,       ;KMMMMMWd.  .O
d      'OMMMMMMWl           ,kNMMMMMMMMMMMMMMMMMMMMMMMMMMMK:.   .cKMMMMMNo.   .O
O.      '0MMMMMN:             ,dKWMMMMMMMMMWX0000KXNMMMMMMMWKkkOXWMMMMWO;     '0
Nc       .kWMMMX;               .,lxOXWMMMWx.   ...':xNMMMMMMMMMMMMMNk:.      ;X
Md        .cKMMWl                    .cKMMMKdc'    ..lXMMMMMMMMWN0xc'         cN
Mx.         .dXMO.                     ,o0WMMMNxcoOKNWMMXkdool:;..            oM
Md            .lx:                       .cxxdllldOXWWXd'                    .OM
Mx.                                        .oxdolcloc,.                      ;XM
M0'                                         .lxOOOxc.                        dMM
MWl                                                 ..                      '0MM
MMK,                                              ,kXKo.                    oWMM
MMMk.               ';.                          ;KMMMWl                   ,KMMM
MMMWd.              ,Ol                         .xMMMMMx.                 .xWMMM
MMMMNo              .xX:                        '0MMMMMk.                 cNMMMM
MMMMMNo.             ,KK;                       ,KMMMMMd                 ,KMMMMM
MMMMMMWk'             oWK,                      '0MMMMWc                .OMMMMMM
MMMMMMMMXd,.          cNM0,                     .kMMMM0'               .kWMMMMMM
MMMMMMMMMMN0xlc:;;;:cdXMMMK;                     cWMMMd               .kWMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMXc                    .OMMMo              :0MMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNx'                   :XMMk.          .:kNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKo.                  cXMWO:.....,:oOXWMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd;.               .OMMMWNKKKXWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxl:,'........,ckWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNX0OOkO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
"""

WWF_output = [('\n', 1), ('M', 31), ('K', 1), ('o', 1), (',', 1), ('.', 1), (' ', 3), ('.', 1), (':', 1), ('d', 1), ('O', 1), ('W', 1), ('M', 37), ('\n', 1), ('M', 29), ('K', 1), ('l', 1), ('.', 1), (' ', 9), ('.', 1), ('o', 1), ('X', 1), ('M', 36), ('\n', 1), ('M', 27), ('W', 1), ('x', 1), ('.', 1), (' ', 13), ('c', 1), ('X', 1), ('M', 21), ('W', 1), ('K', 1), ('k', 1), ('o', 1), ('l', 2), ('o', 1), ('x', 1), ('K', 1), ('W', 1), ('M', 4), ('\n', 1), ('M', 27), ('k', 1), ('.', 1), (' ', 15), ('o', 1), ('W', 1), ('M', 18), ('W', 1), ('O', 1), (';', 1), ('.', 1), (' ', 6), ('.', 1), (',', 1), ('x', 1), ('X', 1), ('M', 2), ('\n', 1), ('M', 26), ('W', 1), ('o', 1), (' ', 16), (';', 1), ('X', 1), ('M', 17), ('N', 1), ('o', 1), ('.', 1), (' ', 11), (',', 1), ('O', 1), ('W', 1), ('\n', 1), ('M', 27), ('k', 1), ('.', 1), (' ', 13), ('.', 1), (';', 1), ('O', 1), ('W', 1), ('M', 16), ('W', 1), ('d', 1), (' ', 14), ("'", 1), ('0', 1), ('\n', 1), ('M', 13), ('W', 1), ('K', 1), ('O', 1), ('0', 1), ('N', 1), ('M', 9), ('W', 1), ('k', 1), ('.', 1), (' ', 7), ('.', 1), (',', 1), ('o', 1), ('d', 1), ('k', 1), ('X', 1), ('W', 1), ('M', 18), ('W', 1), ('l', 1), (' ', 15), ('d', 1), ('\n', 1), ('M', 10), ('W', 1), ('X', 1), ('x', 1), ('l', 1), ('d', 1), ('k', 1), ('X', 1), ('M', 9), ('N', 1), ('O', 1), ('c', 1), ('.', 1), (' ', 1), ('.', 1), (' ', 3), ('.', 1), ('l', 1), ('O', 1), ('W', 1), ('M', 24), ('X', 1), ('x', 1), ('c', 1), ("'", 1), (' ', 11), ('.', 1), ('k', 1), ('\n', 1), ('M', 8), ('W', 1), ('O', 1), ('c', 1), (',', 1), ('c', 1), ('0', 1), ('W', 1), ('M', 9), ('N', 1), ('x', 1), (',', 1), (' ', 2), ('.', 1), ('x', 1), ('K', 1), ('0', 1), ('k', 1), ('O', 1), ('X', 1), ('M', 30), ('N', 1), ('k', 1), (':', 1), ('.', 1), (' ', 7), ('.', 1), ('x', 1), ('W', 1), ('\n', 1), ('M', 6), ('W', 1), ('O', 1), (';', 1), ('.', 1), (',', 1), ('O', 1), ('W', 1), ('M', 9), ('N', 1), ('x', 1), ("'", 1), (' ', 3), (',', 1), ('0', 1), ('M', 38), ('W', 1), ('O', 1), (';', 1), (' ', 4), ('.', 1), ('l', 1), ('K', 1), ('M', 2), ('\n', 1), ('M', 5), ('K', 1), ('c', 1), ('.', 2), ('l', 1), ('X', 1), ('M', 9), ('W', 1), ('O', 1), (';', 1), (' ', 4), (';', 1), ('K', 1), ('M', 41), ('N', 1), ('O', 1), ('x', 1), ('d', 1), ('O', 1), ('X', 1), ('M', 4), ('\n', 1), ('M', 3), ('W', 1), ('k', 1), ("'", 1), (' ', 1), ('.', 1), ('d', 1), ('W', 1), ('M', 9), ('N', 1), ('d', 1), ('.', 1), (' ', 4), (',', 1), ('K', 1), ('M', 52), ('\n', 1), ('M', 2), ('W', 1), ('x', 1), ('.', 1), (' ', 2), ('o', 1), ('W', 1), ('M', 9), ('N', 1), ('o', 1), ('.', 1), (' ', 4), ('.', 1), ('O', 1), ('M', 53), ('\n', 1), ('M', 1), ('W', 1), ('x', 1), ('.', 1), (' ', 2), (':', 1), ('X', 1), ('M', 9), ('W', 1), ('d', 1), ('.', 1), (' ', 5), ('l', 1), ('W', 1), ('M', 53), ('\n', 1), ('M', 1), ('O', 1), ('.', 1), (' ', 2), ('.', 1), ('x', 1), ('M', 10), ('O', 1), ('.', 1), (' ', 5), ('.', 1), ('k', 1), ('M', 10), ('N', 1), ('0', 1), ('d', 1), ('l', 3), ('o', 1), ('O', 1), ('N', 1), ('M', 35), ('\n', 1), ('N', 1), ('c', 1), (' ', 3), (',', 1), ('K', 1), ('M', 9), ('W', 1), ('c', 1), (' ', 6), (',', 1), ('K', 1), ('M', 8), ('N', 1), ('x', 1), (',', 1), ('.', 1), (' ', 6), (':', 1), ('K', 1), ('M', 12), ('N', 1), ('0', 1), ('O', 2), ('K', 1), ('W', 1), ('M', 12), ('W', 2), ('M', 2), ('\n', 1), ('O', 1), ('.', 1), (' ', 3), (':', 1), ('N', 1), ('M', 9), ('0', 1), ("'", 1), (' ', 6), (';', 1), ('X', 1), ('M', 7), ('0', 1), (';', 1), (' ', 10), ('c', 1), ('N', 1), ('M', 9), ('N', 1), ('k', 1), (',', 1), ('.', 1), (' ', 2), ('.', 1), (',', 1), ('d', 1), ('X', 1), ('M', 10), ('O', 1), ('d', 1), ('X', 1), ('M', 1), ('\n', 1), ('o', 1), (' ', 4), (':', 1), ('N', 1), ('M', 9), ('k', 1), ('.', 1), (' ', 6), ("'", 1), ('0', 1), ('M', 6), ('K', 1), (';', 1), (' ', 11), ("'", 1), ('0', 1), ('M', 8), ('N', 1), ('o', 1), ('.', 1), (' ', 7), (',', 1), ('0', 1), ('M', 9), ('d', 1), ("'", 1), ('x', 1), ('M', 1), ('\n', 1), (':', 1), (' ', 4), (',', 1), ('K', 1), ('M', 9), ('x', 1), ('.', 1), (' ', 6), ('.', 1), ('x', 1), ('M', 6), ('x', 1), ('.', 1), (' ', 10), ('.', 1), ('o', 1), ('X', 1), ('M', 8), ('x', 1), ('.', 1), (' ', 9), (',', 1), ('K', 1), ('M', 7), ('W', 1), ('l', 1), (' ', 1), ('c', 1), ('W', 1), ('\n', 1), (';', 1), (' ', 4), ('.', 1), ('k', 1), ('M', 9), ('x', 1), ('.', 1),
(' ', 7), (':', 1), ('X', 1), ('M', 5), ('O', 1), ('.', 1), (' ', 9), (';', 1), ('0', 1), ('W', 1), ('M', 9), ('K', 1), (';', 1), (' ', 9), ('.', 1), ('x', 1), ('M', 7), ('K', 1), (',', 1), (' ', 1), (';', 1), ('X', 1), ('\n', 1), (';', 1), (' ', 5), ('c', 1), ('N', 1), ('M', 8), ('x', 1), ('.', 1), (' ', 8), ('l', 1), ('N', 1), ('M', 4), ('W', 1), ('x', 1), ('.', 1), (' ', 6), ("'", 1), ('d', 1), ('N', 1), ('M', 12), ('K', 1), (';', 1), (' ', 8), ('.', 1), ('x', 1), ('M', 6), ('W', 1), ('l', 1), (' ', 2), ("'", 1), ('0', 1), ('\n', 1), ('c', 1), (' ', 5), ('.', 1), ('x', 1), ('W', 1), ('M', 7), ('x', 1), ('.', 1), (' ', 9), ('c',
1), ('X', 1), ('M', 4), ('W', 1), ('K', 1), ('d', 1), ('l', 1), ('c', 1), ('l', 1), ('k', 1), ('0', 1), ('X', 1), ('M', 15), ('0', 1), (',', 1), (' ', 7), (';', 1), ('K', 1), ('M', 5), ('W', 1), ('d', 1), ('.', 1), (' ', 2), ('.', 1), ('O', 1), ('\n', 1), ('d', 1), (' ', 6), ("'", 1), ('O', 1), ('M', 6), ('W', 1), ('l', 1), (' ', 11), (',', 1), ('k', 1), ('N', 1), ('M', 27), ('K', 1), (':', 1), ('.', 1), (' ', 3), ('.', 1), ('c', 1), ('K', 1), ('M', 5), ('N', 1), ('o', 1), ('.', 1), (' ', 3), ('.', 1), ('O', 1), ('\n', 1), ('O', 1), ('.', 1), (' ', 6), ("'", 1), ('0', 1), ('M', 5), ('N', 1), (':', 1), (' ', 13), (',', 1), ('d', 1), ('K', 1), ('W', 1), ('M', 9), ('W', 1), ('X', 1), ('0', 4), ('K', 1), ('X', 1), ('N', 1), ('M', 7), ('W', 1), ('K', 1), ('k', 2), ('O', 1), ('X', 1), ('W', 1), ('M', 4), ('W', 1), ('O', 1), (';', 1), (' ', 5), ("'", 1), ('0', 1), ('\n', 1), ('N', 1), ('c', 1), (' ', 7), ('.', 1), ('k', 1), ('W', 1), ('M', 3), ('X', 1), (';', 1), (' ', 15), ('.', 1), (',', 1), ('l', 1), ('x', 1), ('O', 1), ('X', 1), ('W', 1), ('M', 3), ('W', 1), ('x', 1), ('.', 1), (' ', 3), ('.', 3), ("'", 1), (':', 1), ('x', 1), ('N', 1), ('M', 13), ('N', 1), ('k', 1), (':', 1), ('.', 1), (' ', 6), (';', 1), ('X', 1), ('\n', 1), ('M', 1), ('d', 1), (' ', 8), ('.', 1), ('c', 1), ('K', 1), ('M', 2), ('W', 1), ('l', 1), (' ', 20), ('.', 1), ('c', 1), ('K', 1), ('M', 3), ('K', 1), ('d', 1), ('c', 1), ("'", 1), (' ', 4), ('.', 2), ('l', 1), ('X', 1), ('M', 8), ('W', 1), ('N',
1), ('0', 1), ('x', 1), ('c', 1), ("'", 1), (' ', 9), ('c', 1), ('N', 1), ('\n', 1), ('M', 1), ('x', 1), ('.', 1), (' ', 9), ('.', 1), ('d', 1), ('X', 1), ('M', 1), ('O', 1), ('.', 1), (' ', 21), (',', 1), ('o', 1), ('0', 1), ('W', 1), ('M', 3), ('N', 1), ('x', 1), ('c', 1), ('o', 1), ('O', 1), ('K', 1), ('N', 1), ('W', 1), ('M', 2), ('X', 1), ('k', 1), ('d', 1), ('o', 2), ('l', 1), (':', 1), (';', 1), ('.', 2), (' ', 12), ('o', 1), ('M', 1), ('\n', 1), ('M', 1), ('d', 1), (' ', 12), ('.', 1), ('l', 1), ('x', 1), (':', 1), (' ', 23), ('.', 1), ('c', 1), ('x', 2), ('d', 1), ('l', 3), ('d', 1), ('O', 1), ('X', 1), ('W', 2), ('X', 1), ('d', 1), ("'", 1), (' ', 20), ('.', 1), ('O', 1), ('M', 1), ('\n', 1), ('M', 1), ('x', 1), ('.', 1), (' ', 40), ('.', 1), ('o', 1), ('x', 1), ('d', 1), ('o', 1), ('l', 1), ('c', 1), ('l', 1), ('o', 1), ('c', 1), (',', 1), ('.', 1), (' ', 22), (';', 1), ('X', 1), ('M', 1), ('\n', 1), ('M', 1), ('0', 1), ("'", 1), (' ', 41), ('.', 1), ('l', 1), ('x', 1), ('O', 3), ('x', 1), ('c', 1), ('.', 1), (' ', 24), ('d', 1), ('M', 2), ('\n', 1), ('M', 1), ('W', 1), ('l', 1), (' ', 49), ('.', 2), (' ', 22), ("'", 1), ('0', 1), ('M', 2), ('\n', 1), ('M', 2), ('K', 1), (',', 1), (' ', 46), (',', 1), ('k', 1), ('X', 1), ('K', 1), ('o', 1), ('.',
1), (' ', 20), ('o', 1), ('W', 1), ('M', 2), ('\n', 1), ('M', 3), ('k', 1), ('.', 1), (' ', 15), ("'", 1), (';', 1), ('.', 1), (' ', 26), (';', 1), ('K', 1), ('M', 3), ('W', 1), ('l', 1), (' ', 19), (',', 1), ('K', 1), ('M', 3), ('\n', 1), ('M', 3), ('W', 1), ('d', 1), ('.', 1), (' ', 14), (',', 1), ('O', 1), ('l', 1), (' ', 25), ('.', 1), ('x', 1), ('M', 5), ('x', 1), ('.', 1), (' ', 17), ('.', 1), ('x', 1), ('W', 1), ('M', 3), ('\n', 1), ('M', 4), ('N', 1), ('o', 1), (' ', 14), ('.', 1), ('x', 1), ('X', 1), (':', 1), (' ', 24), ("'", 1), ('0', 1), ('M', 5), ('k', 1), ('.', 1), (' ', 17), ('c', 1), ('N', 1), ('M', 4), ('\n', 1), ('M', 5), ('N', 1), ('o', 1), ('.', 1), (' ', 13), (',', 1), ('K', 2), (';', 1), (' ', 23), (',', 1), ('K', 1), ('M', 5), ('d', 1), (' ', 17), (',', 1), ('K', 1), ('M', 5), ('\n', 1), ('M', 6), ('W', 1), ('k', 1),
("'", 1), (' ', 13), ('o', 1), ('W', 1), ('K', 1), (',', 1), (' ', 22), ("'", 1), ('0', 1), ('M', 4), ('W', 1), ('c', 1), (' ', 16), ('.', 1), ('O', 1), ('M', 6), ('\n', 1), ('M', 8), ('X', 1), ('d', 1), (',', 1), ('.', 1), (' ', 10), ('c', 1), ('N', 1), ('M', 1), ('0', 1), (',', 1), (' ', 21), ('.', 1), ('k', 1), ('M', 4), ('0', 1), ("'", 1), (' ', 15), ('.', 1), ('k', 1), ('W', 1), ('M', 6), ('\n', 1), ('M', 10), ('N', 1), ('0', 1), ('x', 1), ('l', 1), ('c', 1), (':', 1), (';', 3), (':', 1), ('c', 1), ('d', 1), ('X', 1), ('M', 3), ('K', 1), (';', 1), (' ', 21), ('c', 1), ('W', 1), ('M', 3), ('d', 1), (' ', 15), ('.', 1), ('k', 1), ('W', 1), ('M', 7), ('\n', 1), ('M', 27), ('X', 1), ('c', 1), (' ', 20), ('.', 1), ('O', 1), ('M', 3), ('o', 1), (' ', 14), (':', 1), ('0', 1), ('M', 9), ('\n', 1), ('M', 28), ('N', 1), ('x', 1), ("'", 1), (' ', 19), (':', 1), ('X', 1), ('M', 2), ('k', 1), ('.', 1), (' ', 10), ('.', 1), (':', 1), ('k', 1), ('N', 1), ('M', 10), ('\n', 1), ('M', 30), ('K', 1), ('o', 1), ('.', 1), (' ', 18), ('c', 1), ('X', 1), ('M', 1), ('W', 1), ('O', 1), (':', 1), ('.', 5), (',', 1), (':', 1), ('o', 1), ('O', 1), ('X', 1), ('W', 1), ('M', 12), ('\n', 1), ('M', 32), ('X', 1), ('d', 1), (';', 1), ('.', 1), (' ', 15), ('.', 1), ('O', 1), ('M', 3), ('W', 1), ('N', 1), ('K', 3), ('X', 1), ('W', 1), ('M', 17), ('\n', 1), ('M', 34), ('W', 1), ('K', 1), ('x', 1), ('l', 1), (':', 1), (',', 1), ("'", 1), ('.', 8), (',', 1), ('c', 1), ('k', 1), ('W', 1), ('M', 27),
('\n', 1), ('M', 39), ('N', 2), ('X', 1), ('0', 1), ('O', 2), ('k', 1), ('O', 1), ('0', 1), ('X', 1), ('W', 1), ('M', 30), ('\n', 1)]


APPLE_input = """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOo:'.  oWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOl'       dMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:.        '0MMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo.         .dWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:          .oNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0c          .xWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx,.        .lKWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWc       .,oKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo...';cd0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWN0kxdoooodk0XWMMMMMNXXXNWMMWX0kdlcccclodk0XWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNOo:'.          .,cdOKNWWWNKkdc,.             .;lkNMMMMMMMMMMMMM
MMMMMMMMMMMMMW0o'                    .',,,'.                      'l0WMMMMMMMMMM
MMMMMMMMMMMW0c.                                                     .lKWMMMMMMMM
MMMMMMMMMMNd.                                                        'xWMMMMMMMM
MMMMMMMMMXc                                                        ,xXMMMMMMMMMM
MMMMMMMMX:                                                       .dNMMMMMMMMMMMM
MMMMMMMWl                                                       ;0MMMMMMMMMMMMMM
MMMMMMMO.                                                      ;KMMMMMMMMMMMMMMM
MMMMMMWl                                                      .OMMMMMMMMMMMMMMMM
MMMMMMK,                                                      cNMMMMMMMMMMMMMMMM
MMMMMM0'                                                      dMMMMMMMMMMMMMMMMM
MMMMMMO.                                                      oMMMMMMMMMMMMMMMMM
MMMMMM0'                                                      :NMMMMMMMMMMMMMMMM
MMMMMMK,                                                      .OMMMMMMMMMMMMMMMM
MMMMMMWc                                                       ;KMMMMMMMMMMMMMMM
MMMMMMMx.                                                       ;0MMMMMMMMMMMMMM
MMMMMMMX;                                                        .dNMMMMMMMMMMMM
MMMMMMMMx.                                                         ,dXWMMMMMMMMM
MMMMMMMMN:                                                           .:xKWMMMMMM
MMMMMMMMM0'                                                             cNMMMMMM
MMMMMMMMMWk.                                                           .OMMMMMMM
MMMMMMMMMMWx.                                                         .xWMMMMMMM
MMMMMMMMMMMWx.                                                       .xWMMMMMMMM
MMMMMMMMMMMMWk.                                                     .kWMMMMMMMMM
MMMMMMMMMMMMMW0,                                                   ,0WMMMMMMMMMM
MMMMMMMMMMMMMMMXl.                                               .lXMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWk,                                             'kWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMXd.                                         .oXMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXd,.         .,:oxkOOO0Okxo:'.         .,oKWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMXx;.    .,oONMMMMMMMMMMMMMNOl,.    .:xXMMMMMMMMMMMMMMMMMMM
"""

APPLE_output = [('\n', 1), ('M', 48), ('N', 1), ('O', 1), ('o', 1), (':', 1), ("'", 1), ('.', 1), (' ', 2), ('o', 1), ('W', 1), ('M', 22), ('\n', 1), ('M', 45), ('W', 1), ('O', 1), ('l', 1), ("'", 1), (' ', 7), ('d', 1), ('M', 23), ('\n', 1), ('M', 43), ('W', 1), ('O', 1), (':', 1), ('.', 1), (' ', 8), ("'", 1), ('0', 1), ('M', 23), ('\n', 1), ('M', 42), ('X', 1), ('o', 1), ('.', 1), (' ', 9), ('.', 1), ('d', 1), ('W', 1), ('M', 23), ('\n', 1), ('M', 41), ('X', 1), (':', 1), (' ', 10), ('.', 1), ('o', 1), ('N', 1), ('M', 24), ('\n', 1), ('M', 39), ('N', 1), ('0', 1), ('c', 1), (' ', 10), ('.', 1), ('x', 1), ('W', 1), ('M', 25), ('\n', 1), ('M', 39), ('x', 1), (',', 1), ('.', 1), (' ', 8), ('.', 1), ('l', 1), ('K', 1), ('W', 1), ('M', 26), ('\n', 1), ('M', 38), ('W', 1), ('c', 1), (' ', 7), ('.', 1), (',', 1), ('o', 1), ('K', 1), ('W', 1), ('M', 28), ('\n', 1), ('M', 38), ('N', 1), ('o', 1), ('.', 3), ("'", 1), (';', 1), ('c', 1), ('d', 1), ('0', 1), ('N', 1), ('M', 31), ('\n', 1), ('M', 19), ('W', 1), ('N', 1), ('0', 1), ('k', 1), ('x', 1), ('d', 1), ('o', 4), ('d', 1), ('k', 1), ('0', 1), ('X', 1), ('W', 1), ('M', 5), ('N', 1), ('X', 3), ('N', 1), ('W', 1), ('M', 2), ('W', 1), ('X', 1), ('0', 1), ('k', 1), ('d', 1), ('l', 1), ('c', 4), ('l', 1), ('o', 1), ('d', 1), ('k',
1), ('0', 1), ('X', 1), ('W', 1), ('M', 16), ('\n', 1), ('M', 16), ('N', 1), ('O', 1), ('o', 1), (':', 1), ("'", 1), ('.', 1), (' ', 10), ('.', 1), (',', 1), ('c', 1), ('d', 1), ('O', 1), ('K', 1), ('N', 1), ('W', 3), ('N', 1), ('K', 1), ('k', 1), ('d', 1), ('c', 1), (',', 1), ('.', 1), (' ', 13), ('.', 1), (';', 1), ('l', 1), ('k', 1), ('N', 1), ('M', 13), ('\n', 1), ('M', 13), ('W', 1), ('0', 1), ('o', 1), ("'", 1), (' ', 20), ('.', 1), ("'", 1), (',', 3), ("'", 1), ('.', 1), (' ', 22), ("'", 1), ('l', 1), ('0', 1), ('W', 1), ('M', 10), ('\n', 1), ('M', 11), ('W', 1), ('0', 1), ('c', 1), ('.', 1), (' ', 53), ('.', 1), ('l', 1), ('K', 1), ('W', 1), ('M', 8), ('\n', 1), ('M', 10), ('N', 1), ('d', 1), ('.', 1), (' ', 56), ("'", 1), ('x', 1), ('W', 1), ('M', 8), ('\n', 1), ('M', 9), ('X', 1), ('c', 1), (' ', 56), (',', 1), ('x', 1), ('X', 1), ('M', 10), ('\n', 1), ('M', 8), ('X', 1), (':', 1), (' ', 55), ('.', 1), ('d', 1), ('N', 1), ('M', 12), ('\n', 1), ('M', 7), ('W', 1), ('l', 1), (' ', 55), (';', 1), ('0', 1), ('M', 14), ('\n', 1), ('M', 7), ('O', 1), ('.', 1), (' ', 54), (';', 1), ('K', 1), ('M', 15), ('\n', 1), ('M', 6), ('W', 1), ('l', 1), (' ', 54), ('.', 1), ('O', 1), ('M', 16), ('\n', 1), ('M', 6), ('K', 1), (',', 1), (' ', 54), ('c', 1), ('N', 1),
('M', 16), ('\n', 1), ('M', 6), ('0', 1), ("'", 1), (' ', 54), ('d', 1), ('M', 17), ('\n', 1), ('M', 6), ('O', 1), ('.', 1), (' ', 54), ('o', 1), ('M', 17), ('\n', 1), ('M', 6), ('0', 1), ("'", 1), (' ', 54), (':', 1), ('N', 1), ('M', 16), ('\n', 1), ('M', 6), ('K', 1), (',', 1), (' ', 54), ('.', 1), ('O', 1), ('M', 16), ('\n', 1), ('M', 6), ('W', 1), ('c', 1), (' ', 55), (';', 1), ('K', 1), ('M', 15), ('\n', 1), ('M', 7), ('x', 1), ('.', 1), (' ', 55), (';', 1), ('0', 1), ('M', 14), ('\n', 1), ('M', 7), ('X', 1), (';', 1), (' ', 56), ('.', 1), ('d', 1), ('N', 1), ('M', 12), ('\n', 1), ('M', 8), ('x', 1), ('.', 1), (' ', 57), (',', 1), ('d', 1), ('X', 1), ('W', 1), ('M', 9), ('\n', 1), ('M', 8), ('N', 1), (':', 1), (' ', 59), ('.', 1), (':', 1), ('x', 1), ('K', 1), ('W', 1), ('M', 6), ('\n', 1), ('M', 9), ('0', 1), ("'", 1), (' ', 61), ('c', 1), ('N', 1), ('M', 6), ('\n', 1), ('M', 9), ('W', 1), ('k', 1), ('.', 1), (' ', 59), ('.', 1), ('O', 1), ('M', 7), ('\n', 1), ('M', 10), ('W', 1), ('x', 1), ('.', 1), (' ', 57), ('.', 1), ('x', 1), ('W', 1), ('M', 7), ('\n', 1), ('M', 11), ('W', 1), ('x', 1), ('.', 1), (' ', 55), ('.', 1), ('x', 1), ('W', 1), ('M', 8), ('\n', 1), ('M', 12), ('W', 1), ('k', 1), ('.', 1), (' ', 53), ('.', 1), ('k', 1), ('W', 1), ('M', 9), ('\n', 1), ('M', 13), ('W', 1), ('0', 1), (',', 1), (' ', 51), (',', 1), ('0', 1), ('W', 1), ('M', 10), ('\n', 1), ('M', 15), ('X', 1), ('l', 1), ('.', 1), (' ', 47), ('.', 1), ('l', 1), ('X', 1), ('M', 12), ('\n', 1), ('M', 16), ('W', 1), ('k', 1), (',', 1), (' ', 45), ("'", 1), ('k', 1), ('W', 1), ('M', 13), ('\n', 1), ('M', 18), ('X', 1), ('d', 1), ('.', 1), (' ', 41), ('.', 1), ('o', 1), ('X', 1), ('M', 15), ('\n', 1), ('M', 20), ('X', 1), ('d', 1), (',', 1), ('.', 1), (' ', 9), ('.', 1), (',', 1), (':', 1), ('o', 1), ('x', 1), ('k', 1), ('O', 3), ('0', 1), ('O', 1), ('k', 1), ('x', 1), ('o', 1), (':', 1), ("'", 1), ('.', 1),
(' ', 9), ('.', 1), (',', 1), ('o', 1), ('K', 1), ('W', 1), ('M', 16), ('\n', 1), ('M', 22), ('X', 1), ('x', 1), (';', 1), ('.', 1), (' ', 4), ('.', 1), (',', 1), ('o', 1), ('O', 1), ('N', 1), ('M', 13), ('N', 1), ('O', 1), ('l', 1), (',', 1), ('.', 1), (' ', 4), ('.', 1), (':', 1), ('x', 1), ('X', 1), ('M', 19), ('\n', 1)]

input_output = [('MMMMaaacXolloMM', [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]),
                ('gggfhhhhhhggg', [('g', 3), ('f', 1), ('h', 6), ('g', 3)]),
                ('~~~~~@@@---@@@~~~~~', [('~', 5), ('@', 3), ('-', 3), ('@', 3), ('~', 5)]) ]
    
@pytest.mark.parametrize("input,expected", input_output)
def test_iterative(input, expected):
    assert artcode_i(input) == expected, input

@pytest.mark.parametrize("input,expected", input_output)
def test_recursive(input, expected):
    assert artcode_r(input) == expected, input

def test_misc():
    assert artcode_i(WWF_input) == WWF_output 
    assert artcode_r(WWF_input) == WWF_output 
    assert artcode_i(APPLE_input) == APPLE_output 
    assert artcode_r(APPLE_input) == APPLE_output 


