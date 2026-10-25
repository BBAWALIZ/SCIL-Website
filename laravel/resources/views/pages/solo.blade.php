@php $c = config('scil.contact'); @endphp
<x-layout :title="__('pages.solo.title')" :desc="__('pages.solo.desc')" active="solo">

<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="{{ route('home') }}">{{ __('ui.home_crumb') }}</a></li><li>{{ __('pages.solo.crumb') }}</li></ol>
    <div class="solo-hero">
      <div><img src="{{ asset('assets/img/brand/solo-logo.png') }}" alt="SOLO" style="height:64px;width:auto;margin-bottom:28px;mix-blend-mode:multiply"><h1 class="sign-xl">{{ __('pages.solo.h1') }}</h1></div>
      <p class="lede">{{ __('pages.solo.lede') }}</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="solo-grid">
      @foreach ($solo as $s)
      <article class="pricecard footprint" id="solo-{{ $s['index'] + 1 }}">
        <div class="plate">
          <div class="pricecard__img"><img class="photo-mult" src="{{ asset('assets/img/products/'.$s['image']) }}" alt="" loading="lazy" width="409" height="334"></div>
          <h2>{{ $s['name'] }}</h2>
          <p>{{ $s['desc'] }}</p>
          <div class="price">@foreach ($s['prices'] as [$k, $v])<span><small>{{ $k }}</small><b dir="ltr">{{ $v }}</b></span>@endforeach</div>
          <p style="margin:16px 0 0;flex:0"><a class="link-arrow" href="https://wa.me/{{ $c['whatsapp'] }}?text={{ rawurlencode(__('pages.solo.wa_text', ['name' => $s['name']])) }}" rel="noopener">{{ __('pages.solo.order_wa') }} <x-icon name="arrow"/></a></p>
        </div></article>
      @endforeach
    </div>
    <p class="fineprint">{{ __('pages.solo.fine') }}</p>
  </div>
</section>

<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">{{ __('pages.solo.enq_title') }}</h2><p class="lede" style="margin-top:20px">{{ __('pages.solo.enq_lede') }}</p></div>
    <div class="zone__form">@include('partials.enquiry-form', ['machine' => __('pages.solo.enq_machine')])</div>
  </div>
</section>

</x-layout>
