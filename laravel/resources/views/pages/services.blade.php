@php
    $c = config('scil.contact');
    $q = [__('ui.quote_open'), __('ui.quote_close')];
@endphp
<x-layout :title="__('pages.services.title')" :desc="__('pages.services.desc')" active="services">

<section class="page-head asphalt" style="padding-bottom:var(--space-section)">
  <div class="wrap">
    <ol class="crumbs" style="color:var(--on-asphalt-2)"><li><a href="{{ route('home') }}" style="color:var(--on-asphalt)">{{ __('ui.home_crumb') }}</a></li><li>{{ __('pages.services.crumb') }}</li></ol>
    <div class="page-head__grid">
      <h1 class="sign-xl" style="color:var(--plate)">{{ __('pages.services.h1') }}</h1>
      <p class="lede">{{ __('pages.services.lede') }}</p>
    </div>
    <ol class="loop" style="padding:0;list-style:none;margin-top:clamp(56px,7vw,96px)">
      @foreach (__('pages.services.loop') as $i => [$h, $p])
        <li class="loop__step @if($i === 4) loop__step--stop @endif"><span class="chip">{{ $i === 4 ? '!' : $i + 1 }}</span><h2>{{ $h }}</h2><p>{{ $p }}</p></li>
      @endforeach
    </ol>
  </div>
</section>

<div class="wrap">
  <section class="svc-block" id="service-packages" aria-labelledby="h-pk">
    <div class="svc-block__head"><h2 class="sign-l" id="h-pk">{!! __('pages.services.audit_title') !!}</h2><img src="{{ asset('assets/img/products/svc2.jpg') }}" alt="{{ __('pages.services.audit_img_alt') }}" loading="lazy"></div>
    <div class="svc-block__body prose">
      <p>{{ __('pages.services.audit_p1') }}</p>
      <p>{{ __('pages.services.audit_p2') }}</p>
      <h3 class="sign-s" style="margin-top:36px;margin-bottom:12px">{{ __('pages.services.overhaul_title') }}</h3>
      <p>{{ __('pages.services.overhaul_p') }}</p>
      <ul class="checks">
        @foreach (__('pages.services.overhaul_checks') as $t)<li><x-icon name="check"/><span>{{ $t }}</span></li>@endforeach
      </ul>
    </div>
  </section>
  <section class="svc-block" id="spare-parts" aria-labelledby="h-sp">
    <div class="svc-block__head"><h2 class="sign-l" id="h-sp">{{ __('pages.services.parts_title') }}</h2><img src="{{ asset('assets/img/products/svc1.jpg') }}" alt="{{ __('pages.services.parts_img_alt') }}" loading="lazy"></div>
    <div class="svc-block__body prose">
      <p>{{ __('pages.services.parts_p') }}</p>
      <ul class="checks">
        <li><x-icon name="check"/><span>{{ __('pages.services.parts_dept') }} <a href="mailto:{{ $c['email_parts'] }}">{{ $c['email_parts'] }}</a></span></li>
        @foreach (__('pages.services.parts_checks') as $t)<li><x-icon name="check"/><span>{{ $t }}</span></li>@endforeach
      </ul>
    </div>
  </section>
  <section class="svc-block" id="training" aria-labelledby="h-tr">
    <div class="svc-block__head"><h2 class="sign-l" id="h-tr">{{ __('pages.services.training_title') }}</h2><img src="{{ asset('assets/img/products/svc3.jpg') }}" alt="{{ __('pages.services.training_img_alt') }}" loading="lazy"></div>
    <div class="svc-block__body prose">
      <p>{{ __('pages.services.training_p') }}</p>
      <ol class="qlist">@foreach (__('pages.services.training_q') as $t)<li>{{ $t }}</li>@endforeach</ol>
      <blockquote class="quote" style="margin-top:36px"><p>{{ $q[0] }}{{ __('pages.services.training_quote') }}{{ $q[1] }}</p><footer>{!! __('pages.services.training_who') !!}</footer></blockquote>
    </div>
  </section>
</div>

<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">{{ __('pages.services.enq_title') }}</h2><p class="lede" style="margin-top:20px">{{ __('pages.services.enq_lede') }}</p>
      @include('partials.direct-links', ['items' => ['whatsapp', 'call_short', 'parts']])</div>
    <div class="zone__form">@include('partials.enquiry-form', ['machine' => __('pages.services.enq_machine')])</div>
  </div>
</section>

</x-layout>
