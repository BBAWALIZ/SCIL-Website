{{-- Container drawings (preform, bottle, pack, pallet...) used across the site with <use href="#tk-..."> --}}
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
 <defs>
  <clipPath id="clip-bottle"><path d="M134 80C134 112 92 130 92 166v62q8 10 0 20v92c0 30 8 44 26 44h64c18 0 26-14 26-44v-92q-8-10 0-20v-62c0-36-42-54-42-86z"/></clipPath>
  <symbol id="tk-preform" viewBox="0 0 300 400">
    <path d="M122 124l2 216c0 30 10 44 26 44s26-14 26-44l2-216z" fill="#c9d9ee" stroke="#141716" stroke-width="3"/>
    <path d="M140 140v190" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"/>
    <rect x="104" y="112" width="92" height="12" fill="#1d58a6" stroke="#141716" stroke-width="3"/>
    <rect x="114" y="98" width="72" height="12" fill="#c9d9ee" stroke="#141716" stroke-width="3"/>
    <rect x="118" y="44" width="64" height="54" fill="#c9d9ee" stroke="#141716" stroke-width="3"/>
    <path d="M118 58l64 6M118 72l64 6M118 86l64 6" stroke="#141716" stroke-width="2.5"/>
    <path d="M70 392h160" stroke="#141716" stroke-width="3"/>
  </symbol>
  <symbol id="tk-bottle-shape" viewBox="0 0 300 400">
    <path d="M134 80C134 112 92 130 92 166v62q8 10 0 20v92c0 30 8 44 26 44h64c18 0 26-14 26-44v-92q-8-10 0-20v-62c0-36-42-54-42-86z" fill="rgba(201,217,238,.45)" stroke="#141716" stroke-width="3"/>
    <rect x="124" y="70" width="52" height="10" fill="#c9d9ee" stroke="#141716" stroke-width="3"/>
    <rect x="132" y="34" width="36" height="36" fill="#c9d9ee" stroke="#141716" stroke-width="3"/>
    <path d="M132 46l36 4M132 58l36 4" stroke="#141716" stroke-width="2.5"/>
    <path d="M110 176v150" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".9"/>
    <path d="M92 228q8 10 0 20M208 228q-8 10 0 20" fill="none" stroke="#141716" stroke-width="3"/>
    <path d="M70 392h160" stroke="#141716" stroke-width="3"/>
  </symbol>
  <symbol id="tk-bottle" viewBox="0 0 300 400"><use href="#tk-bottle-shape"/></symbol>
  <symbol id="tk-filled" viewBox="0 0 300 400">
    <g clip-path="url(#clip-bottle)"><path d="M60 150q30-10 60 0t60 0 60 0V400H60z" fill="#7fb0e6"/></g>
    <use href="#tk-bottle-shape"/>
    <rect x="128" y="22" width="44" height="50" fill="#1d58a6" stroke="#141716" stroke-width="3"/>
    <path d="M136 22v50M146 22v50M156 22v50M164 22v50" stroke="#141716" stroke-width="1.5" opacity=".55"/>
  </symbol>
  <symbol id="tk-labelled" viewBox="0 0 300 400">
    <use href="#tk-filled"/>
    <rect x="92" y="258" width="116" height="74" fill="#f4f5f1" stroke="#141716" stroke-width="3"/>
    <path d="M106 278h60M106 292h88M106 306h44" stroke="#1d58a6" stroke-width="5"/>
  </symbol>
  <symbol id="tk-mini" viewBox="0 0 120 220">
    <g transform="scale(.4) translate(0 150)"><use href="#tk-labelled" width="300" height="400"/></g>
  </symbol>
  <symbol id="tk-pack" viewBox="0 0 300 400">
    <g transform="translate(36 120) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <g transform="translate(86 120) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <g transform="translate(136 120) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <g transform="translate(14 150) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <g transform="translate(64 150) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <g transform="translate(114 150) scale(.42)"><use href="#tk-labelled" width="300" height="400"/></g>
    <path d="M40 176c0-14 8-18 20-18h170c14 0 24 4 24 18v190c0 12-8 18-20 18H60c-12 0-20-6-20-18z" fill="rgba(255,255,255,.28)" stroke="#141716" stroke-width="3"/>
    <path d="M58 200c40 10 140 10 180 0M58 360c40 8 140 8 180 0" stroke="#fff" stroke-width="4" opacity=".7" fill="none"/>
    <path d="M30 392h240" stroke="#141716" stroke-width="3"/>
  </symbol>
  <symbol id="tk-pallet" viewBox="0 0 300 400">
    <g stroke="#141716" stroke-width="3">
      <rect x="34" y="350" width="232" height="12" fill="#f4f5f1"/>
      <rect x="40" y="362" width="28" height="18" fill="#f4f5f1"/><rect x="136" y="362" width="28" height="18" fill="#f4f5f1"/><rect x="232" y="362" width="28" height="18" fill="#f4f5f1"/>
      <rect x="34" y="380" width="232" height="10" fill="#f4f5f1"/>
      <g fill="#cfe5d6">
        <rect x="40" y="280" width="72" height="70"/><rect x="112" y="280" width="76" height="70"/><rect x="188" y="280" width="72" height="70"/>
        <rect x="40" y="210" width="72" height="70"/><rect x="112" y="210" width="76" height="70"/><rect x="188" y="210" width="72" height="70"/>
        <rect x="40" y="140" width="72" height="70"/><rect x="112" y="140" width="76" height="70"/><rect x="188" y="140" width="72" height="70"/>
      </g>
    </g>
    <path d="M40 140h220v210H40z" fill="none" stroke="#11784a" stroke-width="5"/>
    <path d="M40 186l220-34M40 246l220-34M40 306l220-34M40 346l220-34" stroke="#11784a" stroke-width="2" opacity=".55"/>
    <path d="M62 300h28M134 300h32M210 300h28M62 230h28M134 230h32M210 230h28M62 160h28M134 160h32M210 160h28" stroke="#141716" stroke-width="3"/>
  </symbol>
  <symbol id="tk-water" viewBox="0 0 300 400">
    <g stroke="#141716" stroke-width="3">
      <rect x="40" y="150" width="56" height="230" rx="28" fill="#c9d9ee"/>
      <rect x="122" y="110" width="56" height="270" rx="28" fill="#c9d9ee"/>
      <rect x="204" y="190" width="56" height="190" rx="28" fill="#7fb0e6"/>
      <path d="M96 200h26M178 240h26" fill="none"/>
    </g>
    <path d="M30 392h240" stroke="#141716" stroke-width="3"/>
  </symbol>
  <symbol id="tk-pallet-mini" viewBox="0 0 64 56">
    <g fill="none" stroke="currentColor" stroke-width="3"><path d="M4 44h56M8 52h48M10 44v8M32 44v8M54 44v8"/><path d="M8 8h48v36H8zM8 26h48M32 8v36"/></g>
  </symbol>
 </defs>
</svg>
