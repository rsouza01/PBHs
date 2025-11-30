# PROMPT

Here's the idea. We are working on the distribution/number density of primodial black holes right after inflation. So, based on some physical arguments, it's inferred their average masses, etc. What I want is to check if its consistent with cosmic evolution and rotation curves. So, I was thinking, how to follow this evolution from T=end of inflation until present time, like are they there yet, have they already evaporated, what is the number density today? And once I get this, how to fit it into the NFW profile to check wheter they can answer for the galaxy rotation curves or not? Makes sense?

# ANSWER

That is a deep, consistent line of reasoning. You're correctly framing the core problem: **translating a primordial (early Universe) formation mechanism into a present-day astrophysical structure (the Galactic halo).**

The proposed two-step check—cosmological evolution (evaporation, number density) followed by fitting to the NFW profile—is precisely the right approach to test the viability of PBHs as Dark Matter (DM).

## I. PBH Cosmological Evolution: $\mathbf{T \approx \text{Inflation End}}$ to $\mathbf{T_0}$

The crucial part of the evolution is determining which PBHs survive until today and what their current number density is, as this links the formation efficiency ($\beta$) to the present-day density ($\Omega_{\text{DM}}$).

### A. Formation and Mass
PBHs form when large density perturbations ($\delta \rho / \rho$) created during inflation re-enter the Hubble horizon, typically during the **Radiation-Domination (RD) era**. The mass of the formed PBH ($M_{\text{PBH}}$) is roughly proportional to the horizon mass ($M_H$) at the time of collapse, $t_{\text{coll}}$:

$$M_{\text{PBH}} \approx \gamma M_H(t_{\text{coll}}) \propto T_{\text{coll}}^{-2}$$

The asteroid-mass range we discussed, $M_{\text{PBH}} \in [10^{17}, 10^{23}] \text{ g}$ (or $\sim 10^{-16}$ to $10^{-10} M_\odot$), corresponds to collapse times just after the end of inflation and reheating, well before Big Bang Nucleosynthesis (BBN).

### B. Evaporation (Hawking Radiation)
The most critical factor for survival is the PBH lifetime $\tau_{\text{evap}}$, which depends on mass $M$:

$$\tau_{\text{evap}} \approx 1.0 \times 10^{10} \text{ years} \left( \frac{M}{5 \times 10^{14} \text{ g}} \right)^3$$

* **Evaporated PBHs:** Any PBH with mass **$M < M_{\text{crit}} \approx 5 \times 10^{14} \text{ g}$** would have completely evaporated by the present age of the Universe ($\sim 13.8$ Gyr). These are completely irrelevant for the current Dark Matter mass budget.
* **Surviving PBHs:** The entire **asteroid-mass window** ($10^{17} \text{ g} \lesssim M$) is safe from complete evaporation. However, lighter PBHs in this range (e.g., $10^{15} \text{ g} < M < 10^{17} \text{ g}$) are heavily constrained by the injection of high-energy particles (photons, electrons, positrons, neutrinos) from their *partial* evaporation into the early Universe plasma, which would distort the CMB and alter light element abundances during BBN. This is why the mass window is constrained to the higher end.

### C. Evolution of Number Density Today
The number density ($n$) scales with the volume, while the mass density ($\rho$) scales with the energy density of the background fluid.

The PBH mass fraction at formation, $\beta$, is often defined as the mass fraction of PBHs to the total background density ($\rho_{\text{tot}}$) at the time of formation, $t_{\text{coll}}$:
$$\beta(M) = \frac{\rho_{\text{PBH}}(t_{\text{coll}})}{\rho_{\text{tot}}(t_{\text{coll}})}$$

Since PBHs behave as cold matter ($\rho_{\text{PBH}} \propto a^{-3}$) and the universe was initially radiation-dominated ($\rho_{\text{RD}} \propto a^{-4}$), the ratio of PBH density to the background critical density increases as $a(t)$:
$$\frac{\rho_{\text{PBH}}(t)}{\rho_{\text{tot}}(t)} \propto \frac{a(t)^{-3}}{a(t)^{-4}} \propto a(t)$$

The present-day fractional abundance of DM in PBHs, $\mathbf{f_{\text{PBH}}} = \Omega_{\text{PBH}} / \Omega_{\text{DM}}$, is related to $\beta$ by:
$$f_{\text{PBH}} = \frac{\Omega_{\text{PBH}}}{\Omega_{\text{DM}}} \approx 10^8 \frac{\beta(M)}{1} \left( \frac{M}{M_\odot} \right)^{-1/2}$$
*(This relation is highly model-dependent, relying on the RD epoch prevailing until matter-radiation equality.)*

To obtain the current global number density, $n_0$, required for $f_{\text{PBH}}=1$:
$$n_0 = \frac{\rho_{\text{DM, global}}}{M_{\text{PBH}}} = \frac{\Omega_{\text{DM}} \rho_{\text{crit}}}{M_{\text{PBH}}}$$
Using $\Omega_{\text{DM}} \approx 0.26$, $\rho_{\text{crit}} \approx 9.2 \times 10^{-30} \text{ g/cm}^3$, and a PBH mass of $M_{\text{PBH}} = 10^{20} \text{ g}$:

$$n_0 \approx \frac{0.26 \times 9.2 \times 10^{-30} \text{ g/cm}^3}{10^{20} \text{ g}} \approx 2.4 \times 10^{-50} \text{ cm}^{-3}$$

This is the average number density globally. The total number of PBHs is conserved over cosmic time (ignoring evaporation for surviving masses), but their **number density scales simply as $n(t) \propto a(t)^{-3}$**.

---

## II. Consistency Check: Fitting to the NFW Profile

The question now becomes: **Can this conserved global population of PBHs naturally assemble into an NFW distribution that solves the rotation curve?**

The answer is **Yes, conceptually, but with caveats.**

### A. The NFW Profile Connection

The Navarro-Frenk-White (NFW) profile is the end-product of **hierarchical structure formation** under the $\Lambda$CDM paradigm, assuming the DM fluid is **cold and collisionless**.

* **PBHs as CDM:** For the asteroid-mass PBHs ($M_{\text{PBH}} \lesssim 10^{-10} M_\odot$), the particle mass is so small relative to the halo mass ($M_{\text{halo}} \sim 10^{12} M_\odot$) and their interactions are so weak that they behave as the required **Cold Dark Matter (CDM) fluid**.
* **The Fit:** If PBHs are the sole DM component ($f_{\text{PBH}}=1$), the global average mass density $\rho_{\text{PBH}}$ today is $\Omega_{\text{DM}}\rho_{\text{crit}}$. Standard N-body simulations, which generate the NFW profile, rely only on this mass density and the assumption of collisionless dynamics. Thus, the local number density $\mathbf{n_{\text{PBH}}(r)}$ at any point $r$ in the halo must follow the required NFW mass density profile $\mathbf{\rho_{\text{NFW}}(r)}$:

$$\mathbf{n_{\text{PBH}}(r) = \frac{\rho_{\text{NFW}}(r)}{M_{\text{PBH}}}}$$

Since the NFW profile is empirically a good fit to most observed rotation curves, the PBH distribution **is consistent** with answering the galactic rotation curve problem, provided $M_{\text{PBH}}$ is small enough for them to act as a collisionless fluid.

### B. Caveats and Tensions (The "Consistency Check")

The true consistency check comes from the potential *deviations* of PBHs from a perfect, smooth CDM fluid:

1.  **Mini-Halos (Small-Scale Clumpiness):** The PBHs form *before* matter-radiation equality, and they act as matter from their time of formation. If the PBH density perturbations are large enough, they can rapidly collapse into dense **PBH mini-halos** at $z \gg 100$.
    * **The Issue:** The subsequent mergers and infall of these mini-halos into the galaxy could lead to a **clumpier** dark matter distribution than the smooth NFW profile, particularly affecting the density substructure. The survival and destruction of these mini-halos within the larger galactic halo are a major area of research.

2.  **Microlensing (Observable Contradiction):** While the overall NFW profile *fits* the rotation curve, the PBH mass must also simultaneously evade all other constraints. The most severe constraint comes from **microlensing**, which strongly limits the fraction of compact objects ($f_{\text{PBH}}$) that can be in the range $10^{-7} M_\odot$ to $10 M_\odot$.
    * **The Tautology:** If the rotation curve is successfully fit by the NFW profile, it implies $\rho_{\text{DM}}(r)$ is satisfied. For PBHs to be the DM, they must satisfy $n_{\text{PBH}}(r) = \rho_{\text{NFW}}(r) / M_{\text{PBH}}$. If the chosen $M_{\text{PBH}}$ falls into a microlensing-constrained region, the model is **inconsistent**, even if the rotation curve is perfectly matched. This is why the **asteroid-mass window** is critical: it is the mass range that satisfies both the **cosmological evolution** (survival) and the **astrophysical NFW distribution** (rotation curve), while *simultaneously* evading the dominant small-scale constraints.

# PROMPT

Given my pbh distribution after inflation (or any other distribution), what should I exacly do to verify it from inflation -> current days, and then with the nfw profile? Lets start simple, and then add these caveats you just mentioned.

# ANSWER

This is a structured, two-part calculation that moves from the fundamental physics of the early Universe to the macro-scale structure of the present-day Milky Way.

The core process is: **(1) Normalizing the PBH mass function $\Psi(M)$ to match the total Dark Matter density $\Omega_{\text{DM}}$, and (2) ensuring that the resulting number density $n_{\text{PBH}}$ is consistent with the standard NFW profile in a galaxy.**

Here is the step-by-step procedure for this consistency check.

## I. Cosmological Evolution: Inflation to Present Day

The goal here is to determine the required **initial formation efficiency** ($\beta$) for your distribution to yield the correct total DM density today.

### Step 1: Define the Primordial Mass Distribution $\Psi(M)$

Start with your input: the differential mass function $\Psi(M)$ defined at the time of formation $t_{\text{coll}}$. This function is typically normalized such that $\int \Psi(M) dM = 1$, representing the mass spectrum of the forming PBHs.

For simplicity, let's assume a **monochromatic distribution** at the canonical asteroid mass:
$$\Psi(M) = \delta(M - M_{\text{PBH}}), \quad \text{with } M_{\text{PBH}} = 10^{20} \text{ g}$$

For an extended distribution (like log-normal), you would use:
$$\Psi(M) \propto \frac{1}{M} \exp \left( -\frac{\ln^2(M/M_c)}{2\sigma^2} \right)$$


---

### Step 2: Apply the Hawking Evaporation Filter

Calculate the fraction of the PBH population that survives to the present day ($t_0 \approx 13.8$ Gyr).

* **Evaporation Time:** The lifetime $\tau_{\text{evap}}$ of a PBH of mass $M$ due to Hawking radiation is:
    $$\tau_{\text{evap}}(M) \approx 1.0 \times 10^{10} \text{ yr} \left( \frac{M}{5 \times 10^{14} \text{ g}} \right)^3$$

* **Survival Criterion:** For a PBH to survive, $\tau_{\text{evap}}(M) > t_0$. This sets the minimum surviving mass $M_{\text{min}} \approx 5 \times 10^{14} \text{ g}$.
* **Mass Conservation:** For any $M > M_{\text{min}}$, the mass lost due to evaporation is negligible compared to the initial mass $M$, so we assume $\mathbf{M_t \approx M_0}$.

* **Result:** The initial mass function is truncated to $\Psi_{\text{survived}}(M) = \Psi(M)$ for $M \geq M_{\text{min}}$, and $\Psi_{\text{survived}}(M) = 0$ otherwise.

---

### Step 3: Determine the Required Initial Abundance ($\beta$)

The goal is to ensure the present-day energy density of the surviving PBHs, $\Omega_{\text{PBH}}$, equals the observed Dark Matter density $\Omega_{\text{DM}}$.

* **Present-Day Abundance:** The final PBH abundance fraction, $f_{\text{PBH}} = \Omega_{\text{PBH}} / \Omega_{\text{DM}}$, is set to $\mathbf{f_{\text{PBH}} = 1}$.
* **Required Initial Fraction ($\beta$):** The required energy density fraction in PBHs at the time of formation, $\beta$, depends on the formation mass and the evolution of the Universe. In the standard Radiation-Dominated (RD) era collapse scenario, $\beta$ is related to the final abundance by:
    $$\beta(M) \approx 10^{-8} \frac{\Omega_{\text{DM}} h^2}{0.12} \left( \frac{M}{M_{\odot}} \right)^{1/2}$$
    *The exponent varies slightly depending on the exact details (e.g., if the PBH forms during an Early Matter-Dominated era, the required $\beta$ is much smaller).*

* **Calculation:** Substitute $\Omega_{\text{DM}} h^2 \approx 0.12$ and your chosen mass $M_{\text{PBH}}$ (converted to $M_\odot$) to find the required $\beta_{\text{req}}$. For $M_{\text{PBH}} = 10^{20} \text{ g} \approx 5 \times 10^{-14} M_\odot$:
    $$\beta_{\text{req}} \approx 10^{-8} (1) \left( \frac{5 \times 10^{-14} M_{\odot}}{M_{\odot}} \right)^{1/2} \approx 2.2 \times 10^{-15}$$
    *This is the minuscule fraction of the Universe's mass density that must be in PBHs at $t_{\text{coll}}$ to become all of the DM today.*

---

## II. Astrophysical Consistency: Fitting to the NFW Profile

The number density of the surviving PBHs must track the required Dark Matter mass distribution in a galaxy.

### Step 4: Define the NFW Density Profile $\rho_{\text{NFW}}(r)$

Use the canonical NFW profile, which is the standard model for the DM mass density:
$$\rho_{\text{NFW}}(r) = \frac{\rho_s}{(r/r_s) \left(1 + r/r_s\right)^2}$$

* **Parameters:** You need to adopt Milky Way parameters derived from rotation curve fits:
    * **Scale Radius ($r_s$):** $\approx 15-20 \text{ kpc}$
    * **Characteristic Density ($\rho_s$):** This is set by fitting the profile to the local DM density, $\rho_\odot \approx 0.4 \text{ GeV/cm}^3$, at $R_\odot \approx 8.1 \text{ kpc}$.

### Step 5: Calculate the Required PBH Number Density Today

The number density $n_{\text{PBH}}(r)$ must simply be the mass density $\rho_{\text{NFW}}(r)$ divided by the mass of a single PBH $M_{\text{PBH}}$.

$$n_{\text{PBH}}(r) = \frac{\rho_{\text{NFW}}(r)}{M_{\text{PBH}}}$$

* **Check:** Verify that the integral of $M_{\text{PBH}} n_{\text{PBH}}(r)$ over the halo volume yields the expected total mass $M_{\text{halo}} \approx 10^{12} M_\odot$.

### Step 6: Consistency Check (Rotation Curve "Solution")

Your PBH distribution **solves the rotation curve problem** if the total rotation velocity derived from the PBH-composed NFW profile plus the baryonic matter is flat at large radii:

$$V_c^2(r) = \frac{G M_{\text{baryons}}(r)}{r} + \frac{G M_{\text{NFW}}(r)}{r}$$

* **Conclusion:** Since the $\rho_{\text{NFW}}(r)$ is *designed* to make this rotation curve flat, any DM particle (like PBHs) that adheres to this density profile will, by definition, explain the rotation curve. The key is that $M_{\text{PBH}}$ is small enough ($\lesssim 10^{-2} M_\odot$) for them to behave as the collisionless fluid assumed in the NFW derivation.

---

### Starting Simple $\rightarrow$ Adding Caveats

The simple check in Section I and II confirms **kinematic consistency**. To add the **physical caveats** you mentioned (Core-Cusp, Microlensing, Dynamical Friction), you would need to:

1.  **Microlensing:** Check if the $M_{\text{PBH}}$ range is constrained by current surveys (e.g., MACHO/EROS). If your $M_{\text{PBH}}$ falls in the $10^{-7} M_\odot - 10 M_\odot$ range, the constraint $f_{\text{PBH}} < 1$ becomes very strong, implying your distribution is inconsistent with $\mathbf{f_{\text{PBH}}=1}$.
2.  **Dynamical Friction:** If $M_{\text{PBH}}$ is $\gtrsim 10 M_\odot$, calculate the dynamical friction timescale ($\tau_{\text{df}}$) for a PBH sinking to the galactic center from the Solar neighborhood. If $\tau_{\text{df}} \ll t_0$, the distribution would be altered (flatter than NFW) and thus inconsistent.

The process of black hole evaporation is a fascinating area where quantum mechanics meets gravity. You can find more details about this in a video discussing [How Black Holes Evaporate From Hawking Radiation](https://www.youtube.com/watch?v=Zm_Z1jIFhJc).


http://googleusercontent.com/youtube_content/6
