@php
    $c = config('scil.contact');
    $heroPick = config('scil.hero_pick');
    $walkPick = config('scil.walk_pick');
    $first = $stations->first();
    $q = [__('ui.quote_open'), __('ui.quote_close')];
@endphp
<x-layout :title="__('pages.home.title')" :desc="__('pages.home.desc')" active="home">

<section class="hero" aria-labelledby="hero-title">
  <div class="wrap">
    <div class="hero__head">
      <h1 class="hero__title" id="hero-title"><span class="sign-xl">{!! __('pages.home.hero') !!}</span></h1>
      <div class="hero__aside">
        <p class="lede">{{ __('pages.home.lede') }}</p>
        <div class="hero__ctas">
          <a class="btn" href="#enquire">{{ __('ui.cta') }} <x-icon name="arrow"/></a>
          <a class="btn btn--plate" href="https://wa.me/{{ $c['whatsapp'] }}" rel="noopener"><x-icon name="chat"/> {{ __('pages.home.wa_engineer') }}</a>
        </div>
      </div>
    </div>
  </div>
  <div class="plan">
    <div class="wrap plan__scroller" tabindex="0" aria-label="{{ __('pages.home.plan_label') }}">
      <div class="plan__track">
        <span class="lane" aria-hidden="true"></span><span class="lane lane--edge" aria-hidden="true"></span><span class="lane-chevrons" aria-hidden="true"></span>
        @foreach ($stations as $i => $s)
        <a class="station-fp footprint" style="--i:{{ $i }}" href="#st-{{ $s['key'] }}">
          <div class="plate">
            <div class="station-fp__no"><span class="stencil">{{ $s['no'] }}</span></div>
            <div class="station-fp__img">
              @isset($heroPick[$s['key']])
                <img class="photo-mult" src="{{ asset('assets/img/products/'.$machines[$heroPick[$s['key']]]['image']) }}" alt="" width="850" height="690">
              @else
                <x-token name="preform"/>
              @endisset
            </div>
            <h2>{{ $s['name'] }}</h2>
            <p>{{ $s['short'] }}</p>
            <span class="mcard__fig">{{ __('pages.home.hero_fig.'.$s['key']) }}</span>
          </div>
        </a>
        @endforeach
        <div class="fg-zone">
          <svg viewBox="0 0 64 56" aria-hidden="true"><use href="#tk-pallet-mini"/></svg>
          <span class="sign-s">{{ __('pages.home.fg_title') }}</span>
          <p>{{ __('pages.home.fg_text') }}</p>
        </div>
      </div>
    </div>
    <p class="wrap plan__hint"><x-icon name="arrow"/> {{ __('pages.home.swipe') }}</p>
  </div>
</section>

<section class="section section--tight" aria-label="{{ __('pages.home.figures_label') }}">
  <div class="wrap">
    <div class="legend">
      <p class="legend__text">{!! __('pages.home.figures') !!}</p>
    </div>
    <p class="legend__foot meta">{{ __('pages.home.figures_foot') }}</p>
  </div>
</section>

<section class="section" id="line" aria-labelledby="line-title" style="padding-top:clamp(40px,5vw,72px)">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="line-title">{{ __('pages.home.walk_title') }}</h2>
      <p class="lede">{{ __('pages.home.walk_lede') }}</p>
    </div>
    <div class="walk" data-walk data-leaves="{{ __('pages.home.leaves') }}">
      <div class="walk__strip" aria-hidden="true"><svg viewBox="0 0 300 400"><use data-strip-use href="#tk-preform"/></svg><strong data-strip-out>01 · {{ $first['out'] }}</strong><div class="walk__strip-lane"><span></span></div></div>
      <div class="walk__rail">
        <div class="walk__sticky">
          <div class="walk__lane" aria-hidden="true"><span class="walk__lane-fill" data-lane-fill></span><ol class="walk__ticks">
            @foreach ($stations as $i => $s)<li style="top:{{ number_format(($i + 0.5) / 6 * 100, 2) }}%" data-tick="{{ $s['no'] }}">{{ $s['no'] }}</li>@endforeach
          </ol></div>
          <div class="walk__ride"><div class="token" aria-hidden="true">
            <div class="token__stage">
              @foreach ($stations as $i => $s)<div class="token__state @if($i === 0) is-on @endif" data-state="{{ $s['token'] }}"><x-token :name="$s['token']"/></div>@endforeach
            </div>
            <div class="token__cap"><strong data-token-out>{{ $first['out'] }}</strong><span class="meta" data-token-no>{{ __('pages.home.leaves') }} 01</span></div>
          </div></div>
        </div>
      </div>
      <div class="stations">
        @foreach ($stations as $s)
        <article class="station" id="st-{{ $s['key'] }}" data-station="{{ $s['no'] }}" data-token="{{ $s['token'] }}" data-out="{{ $s['out'] }}">
          <div class="station__head"><span class="station__no stencil" aria-hidden="true">{{ $s['no'] }}</span><h3 class="sign-m"><span class="visually-hidden">{{ __('pages.home.station_sr', ['no' => $s['no']]) }}</span>{{ $s['name'] }}</h3></div>
          <div class="station__body"><p class="prose">{{ $s['text'] }}</p><x-token :name="$s['token']" class="station__token-inline" :label="__('pages.home.leaves_as', ['out' => $s['out']])"/></div>
          @if (! empty($walkPick[$s['key']]))
            <div class="machines">
              @foreach ($walkPick[$s['key']] as $id)
                @include('partials.mcard', ['m' => $machines[$id], 'heading' => 'h4'])
              @endforeach
            </div>
            @if ($s['key'] === 'filling')
              <p class="meta" style="margin-top:18px">{!! __('pages.home.water_feed', ['url' => route('machine', ['slug' => 'water-treatment-equipment'])]) !!}</p>
            @endif
            <p class="station__more"><a class="link-arrow" href="{{ route('equipment') }}#{{ $s['key'] }}">{{ __('pages.home.all_machines', ['count' => $counts[$s['key']] ?? 0, 'name' => mb_strtolower($s['name'])]) }} <x-icon name="arrow"/></a></p>
          @else
            <div class="empty-bay" style="margin-top:28px"><x-token name="preform"/>
              <p>{!! __('pages.home.injection_empty') !!}</p></div>
            <p class="station__more"><a class="link-arrow" href="{{ route('contact') }}">{{ __('pages.home.injection_ask') }} <x-icon name="arrow"/></a></p>
          @endif
        </article>
        @endforeach
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="proof-title" style="padding-top:0">
  <div class="wrap">
    <div class="proof">
      <div class="proof__lead"><h2 class="sign-l" id="proof-title"><span>{{ __('pages.home.proof_rated') }}</span><span class="go">{{ __('pages.home.proof_running') }}</span></h2></div>
      <figure class="proof__quote">
        <blockquote class="quote"><p>{{ $q[0] }}{{ __('pages.home.proof_quote') }}{{ $q[1] }}</p></blockquote>
        <figcaption class="quote"><footer>{!! __('pages.home.proof_who') !!}</footer></figcaption>
      </figure>
      <div class="gauge" data-gauge role="img" aria-label="{{ __('pages.home.gauge_label') }}">
        <div class="gauge__row"><span class="gauge__lab">{{ __('pages.home.gauge_rated') }}</span><div class="gauge__bar"><div class="gauge__fill gauge__fill--rated" style="--w:70.0%">1,400</div></div></div>
        <div class="gauge__row"><span class="gauge__lab">{{ __('pages.home.gauge_run') }}</span><div class="gauge__bar"><div class="gauge__fill gauge__fill--run" style="--w:90.0%">1,800</div></div></div>
        <div class="gauge__scale"><span></span><div class="gauge__ticks"><span>0</span><span>500</span><span>1,000</span><span>1,500</span><span>{{ __('pages.home.gauge_unit') }}</span></div></div>
      </div>
    </div>

    <div class="returns">
      <div class="returns__txt">
        <h3 class="sign-m">{{ __('pages.home.returns_title') }}</h3>
        <p class="prose" style="margin-top:14px">{{ __('pages.home.returns_text') }}</p>
      </div>
      <div class="returns__path">
        <div class="ret-step"><span class="ret-step__yr">{{ __('pages.home.ret1_yr') }}</span><span class="stencil">12,000 BPH</span><p>{{ __('pages.home.ret1_text') }}</p></div>
        <div class="ret-step"><span class="ret-step__yr">{{ __('pages.home.ret2_yr') }}</span><span class="stencil">24,000 BPH</span><p>{{ __('pages.home.ret2_text') }}</p></div>
      </div>
    </div>

    <div class="tags">
      <div class="sec-head" style="margin-bottom:24px">
        <h3 class="sign-m">{{ __('pages.home.words_title') }}</h3>
        @php $rtl = \App\Support\Locales::current()['dir'] === 'rtl'; @endphp
        <div class="tags__ctrl" style="justify-self:end"><button type="button" data-tags="{{ $rtl ? 1 : -1 }}" aria-label="{{ __('pages.home.prev') }}"><x-icon name="arrow-l"/></button><button type="button" data-tags="{{ $rtl ? -1 : 1 }}" aria-label="{{ __('pages.home.next') }}"><x-icon name="arrow"/></button></div>
      </div>
      <div class="tags__row" data-tags-row tabindex="0" aria-label="{{ __('pages.home.testimonials_label') }}">
        @foreach ($testimonials as $t)
        <article class="tag">
          <div class="tag__band" aria-hidden="true"></div>
          <blockquote><p>{{ $q[0] }}{{ $t['short'] }}{{ $q[1] }}</p>
            <details><summary>{{ __('pages.home.full_words') }} <x-icon name="arrow"/></summary>@foreach ($t['full'] as $p)<p>{{ $p }}</p>@endforeach</details>
          </blockquote>
          <footer><b>{{ $t['org'] }}</b>{{ $t['name'] }}{{ __('ui.list_sep') }}{{ $t['role'] }}</footer>
        </article>
        @endforeach
      </div>
    </div>
  </div>
</section>

<section class="section asphalt" aria-labelledby="svc-title">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="svc-title">{{ __('pages.home.svc_title') }}</h2>
      <p class="lede">{{ __('pages.home.svc_lede') }}</p>
    </div>
    <ol class="loop" style="padding:0;list-style:none">
      @foreach (__('pages.home.loop') as $i => [$h, $p])
        <li class="loop__step @if($i === 4) loop__step--stop @endif"><span class="chip">{{ $i === 4 ? '!' : $i + 1 }}</span><h3>{{ $h }}</h3><p>{{ $p }}</p></li>
      @endforeach
    </ol>
    <div class="bays">
      <div class="bay"><div><h3>{{ __('pages.home.bay_parts_title') }}</h3><p>{{ __('pages.home.bay_parts_text') }}</p><a class="link-arrow" href="{{ route('services') }}#spare-parts">{{ __('pages.home.bay_parts_link') }} <x-icon name="arrow"/></a></div><img src="{{ asset('assets/img/products/svc1.jpg') }}" alt="" loading="lazy"></div>
      <div class="bay"><div><h3>{{ __('pages.home.bay_training_title') }}</h3><p>{{ __('pages.home.bay_training_text') }}</p><a class="link-arrow" href="{{ route('services') }}#training">{{ __('pages.home.bay_training_link') }} <x-icon name="arrow"/></a></div><img src="{{ asset('assets/img/products/svc3.jpg') }}" alt="" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="clients-title">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="clients-title">{{ __('pages.home.clients_title') }}</h2>
      <p class="lede">{{ __('pages.home.clients_lede') }}</p>
    </div>
    <ul class="dock" aria-label="{{ __('pages.home.clients_label') }}">
      @foreach ($logos as $f)<li><img src="{{ asset('assets/img/clients/'.$f) }}" alt="" loading="lazy"></li>@endforeach
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="solo-title" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="sign-l" id="solo-title">{{ __('pages.home.solo_title') }}</h2>
      <p class="lede">{{ __('pages.home.solo_lede') }}</p>
    </div>
    <div class="solo-row">
      @foreach ($soloPick as $s)
      <a class="pricecard footprint" href="{{ route('solo') }}#solo-{{ $s['index'] + 1 }}">
        <div class="plate">
          <div class="pricecard__img"><img class="photo-mult" src="{{ asset('assets/img/products/'.$s['image']) }}" alt="" loading="lazy" width="409" height="334"></div>
          <h3>{{ $s['name'] }}</h3>
          <p>{{ $s['desc'] }}</p>
          <div class="price">@foreach (array_slice($s['prices'], 0, 2) as [$k, $v])<span><small>{{ $k }}</small><b dir="ltr">{{ $v }}</b></span>@endforeach</div>
        </div></a>
      @endforeach
    </div>
    <p class="fineprint">{{ __('pages.home.solo_fine') }}</p>
    <p style="margin-top:24px"><a class="link-arrow" href="{{ route('solo') }}">{{ __('pages.home.solo_all', ['count' => $soloCount]) }} <x-icon name="arrow"/></a></p>
  </div>
</section>

<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt">
      <h2 class="sign-l" id="enq-title">{{ __('pages.home.enq_title') }}</h2>
      <p class="lede" style="margin-top:20px">{{ __('pages.home.enq_lede') }}</p>
      @include('partials.direct-links', ['items' => ['whatsapp', 'call', 'email', 'catalogue']])
    </div>
    <div class="zone__form">@include('partials.enquiry-form')</div>
  </div>
</section>

</x-layout>
