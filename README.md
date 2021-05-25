# invisibility_cloak

This project tries to emulate the invisibility cloak seen in harry potter series.

A cloak is taken as shown in cloak.jpg image. YUV colorspace is used to get thresholds for each channel for the cloak.

Once thresholds are found, mask has been generated based on them. Bitwise-and operation happens between generated mask and background image. This results in an image where each cloak pixel assumes background image part and each non cloak pixel becomes black (0). [background mask] ------ (1)

Bitwise-not operation is applied on the mask which converts all cloak pixels to black (0) and all non cloak to white (255) [inverse background mask]

Bitwise-and operation is applied on inverse background and current frame, this converts all non-cloak pixels to current frame pixels and all cloak pixels to black (0) ------- (2)

(1) and (2) are added and we get background for cloak pixels and current frame for non - cloak pixels



