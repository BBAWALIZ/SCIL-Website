@php $c = config('scil.contact'); @endphp
<x-layout :title="__('pages.about.title')" :desc="__('pages.about.desc')" active="about">

<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="{{ route('home') }}">{{ __('ui.home_crumb') }}</a></li><li>{{ __('pages.about.crumb') }}</li></ol>
    <div class="page-head__grid">
      <h1 class="sign-xl">{{ __('pages.about.h1') }}</h1>
      <p class="lede">{{ __('pages.about.lede') }}</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="legend"><p class="legend__text">{!! __('pages.about.figures') !!}</p></div>
    <div class="sec-head" style="margin-top:clamp(56px,7vw,96px)">
      <div class="prose">
        <p>{{ __('pages.about.p1') }}</p>
        <p>{{ __('pages.about.p2') }}</p>
      </div>
      <div class="footprint"><div class="plate" style="padding:18px"><img class="photo-mult" src="{{ asset('assets/img/brand/prod-line.png') }}" alt="{{ __('pages.about.line_alt') }}" loading="lazy"></div></div>
    </div>
    <div class="vm">
      <div><h2>{{ __('pages.about.vision_t') }}</h2><p>{{ __('pages.about.vision') }}</p></div>
      <div><h2>{{ __('pages.about.mission_t') }}</h2><p>{{ __('pages.about.mission') }}</p></div>
      <div><h2>{{ __('pages.about.resp_t') }}</h2><p>{{ __('pages.about.resp') }}</p></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="team-title">
  <div class="wrap">
    <div class="sec-head"><h2 class="sign-l" id="team-title">{{ __('pages.about.team_title') }}</h2><p class="lede">{{ __('pages.about.team_lede') }}</p></div>
    <ul class="team" style="padding:0;margin:0">
      @foreach ($team as $p)
        <li class="badge"><div class="badge__top" aria-hidden="true"></div><img src="{{ asset('assets/img/team/'.$p['image']) }}" alt="" loading="lazy" width="260" height="285"><div class="badge__txt"><b>{{ $p['name'] }}@if($p['name_zh'] && $p['name_zh'] !== $p['name']) <span lang="zh-Hans">{{ $p['name_zh'] }}</span>@endif</b><span>{{ $p['role'] }}</span></div></li>
      @endforeach
    </ul>
  </div>
</section>

<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">{{ __('pages.about.enq_title') }}</h2><address class="lede" style="margin-top:20px;font-style:normal" dir="ltr">{!! implode('<br>', array_map('e', $c['address'])) !!}</address>
      @include('partials.direct-links', ['items' => ['whatsapp', 'call_short']])</div>
    <div class="zone__form">@include('partials.enquiry-form')</div>
  </div>
</section>

</x-layout>
