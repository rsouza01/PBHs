This is a structured, two-part calculation that moves from the fundamental physics of the early Universe to the macro-scale structure of the present-day Milky Way.

The core process is: **(1) Normalizing the PBH mass function  to match the total Dark Matter density , and (2) ensuring that the resulting number density  is consistent with the standard NFW profile in a galaxy.**

Here is the step-by-step procedure for this consistency check.

## I. Cosmological Evolution: Inflation to Present Day

The goal here is to determine the required **initial formation efficiency** () for your distribution to yield the correct total DM density today.

### Step 1: Define the Primordial Mass Distribution 

Start with your input: the differential mass function  defined at the time of formation . This function is typically normalized such that , representing the mass spectrum of the forming PBHs.

For simplicity, let's assume a **monochromatic distribution** at the canonical asteroid mass:


For an extended distribution (like log-normal), you would use:


---

### Step 2: Apply the Hawking Evaporation Filter

Calculate the fraction of the PBH population that survives to the present day ( Gyr).

* **Evaporation Time:** The lifetime  of a PBH of mass  due to Hawking radiation is:


* **Survival Criterion:** For a PBH to survive, . This sets the minimum surviving mass .
* **Mass Conservation:** For any , the mass lost due to evaporation is negligible compared to the initial mass , so we assume .
* **Result:** The initial mass function is truncated to  for , and  otherwise.

---

### Step 3: Determine the Required Initial Abundance ()

The goal is to ensure the present-day energy density of the surviving PBHs, , equals the observed Dark Matter density .

* **Present-Day Abundance:** The final PBH abundance fraction, , is set to .
* **Required Initial Fraction ():** The required energy density fraction in PBHs at the time of formation, , depends on the formation mass and the evolution of the Universe. In the standard Radiation-Dominated (RD) era collapse scenario,  is related to the final abundance by:



*The exponent varies slightly depending on the exact details (e.g., if the PBH forms during an Early Matter-Dominated era, the required  is much smaller).*
* **Calculation:** Substitute  and your chosen mass  (converted to ) to find the required . For :



*This is the minuscule fraction of the Universe's mass density that must be in PBHs at  to become all of the DM today.*

---

## II. Astrophysical Consistency: Fitting to the NFW Profile

The number density of the surviving PBHs must track the required Dark Matter mass distribution in a galaxy.

### Step 4: Define the NFW Density Profile 

Use the canonical NFW profile, which is the standard model for the DM mass density:


* **Parameters:** You need to adopt Milky Way parameters derived from rotation curve fits:
* **Scale Radius ():** 
* **Characteristic Density ():** This is set by fitting the profile to the local DM density, , at .



### Step 5: Calculate the Required PBH Number Density Today

The number density  must simply be the mass density  divided by the mass of a single PBH .

* **Check:** Verify that the integral of  over the halo volume yields the expected total mass .

### Step 6: Consistency Check (Rotation Curve "Solution")

Your PBH distribution **solves the rotation curve problem** if the total rotation velocity derived from the PBH-composed NFW profile plus the baryonic matter is flat at large radii:

* **Conclusion:** Since the  is *designed* to make this rotation curve flat, any DM particle (like PBHs) that adheres to this density profile will, by definition, explain the rotation curve. The key is that  is small enough () for them to behave as the collisionless fluid assumed in the NFW derivation.

---

### Starting Simple  Adding Caveats

The simple check in Section I and II confirms **kinematic consistency**. To add the **physical caveats** you mentioned (Core-Cusp, Microlensing, Dynamical Friction), you would need to:

1. **Microlensing:** Check if the  range is constrained by current surveys (e.g., MACHO/EROS). If your  falls in the  range, the constraint  becomes very strong, implying your distribution is inconsistent with .
2. **Dynamical Friction:** If  is , calculate the dynamical friction timescale () for a PBH sinking to the galactic center from the Solar neighborhood. If , the distribution would be altered (flatter than NFW) and thus inconsistent.

The process of black hole evaporation is a fascinating area where quantum mechanics meets gravity. You can find more details about this in a video discussing [How Black Holes Evaporate From Hawking Radiation](https://www.youtube.com/watch?v=Zm_Z1jIFhJc).