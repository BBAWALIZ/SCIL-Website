<x-layout :title="__('pages.equipment.title')" :desc="__('pages.equipment.desc')" active="equipment">
@php $all = $stations->concat([$water]); @endphp

<section class="page-head">
  <div class="wrap">
    <ol class="crumbs"><li><a href="{{ route('home') }}">{{ __('ui.home_crumb') }}</a></li><li>{{ __('pages.equipment.crumb') }}</li></ol>
    <div class="page-head__grid">
      <h1 class="sign-xl">{{ __('pages.equipment.h1') }}</h1>
      <p class="lede">{{ __('pages.equipment.lede', ['count' => $machines->count()]) }}</p>
    </div>
  </div>
</section>

<nav class="selector" aria-label="{{ __('pages.equipment.stations_label') }}"><div class="wrap selector__in" data-selector>
  @foreach ($all as $s)
    <a href="#{{ $s['key'] }}" data-sel="{{ $s['key'] }}"><span class="stencil">{{ $s['no'] }}</span>{{ $s['name'] }} <span class="data">{{ $machines->where('station', $s['key'])->count() }}</span></a>
  @endforeach
</div></nav>

<div class="wrap">
  @foreach ($all as $s)
    @php $ms = $machines->where('station', $s['key']); @endphp
    <section class="cat-station" id="{{ $s['key'] }}" data-cat="{{ $s['key'] }}" aria-labelledby="h-{{ $s['key'] }}">
      <div class="cat-station__head"><span class="stencil" aria-hidden="true">{{ $s['no'] }}</span><h2 class="sign-l" id="h-{{ $s['key'] }}">{{ $s['name'] }}</h2><p class="prose">{{ $s['text'] }} <span class="meta" style="display:block;margin-top:8px">{{ __('pages.equipment.leaves_as', ['out' => $s['out']]) }}</span></p></div>
      @if ($ms->isNotEmpty())
        <div class="cat-grid">
          @foreach ($ms as $m) @include('partials.mcard', ['m' => $m, 'heading' => 'h3']) @endforeach
        </div>
      @else
        <div class="empty-bay"><x-token name="preform"/><p>{!! __('pages.equipment.injection_empty', ['url' => route('contact')]) !!}</p></div>
      @endif
    </section>
  @endforeach
</div>

<section class="zone" id="enquire" aria-labelledby="enq-title">
  <div class="wrap zone__grid">
    <div class="zone__txt"><h2 class="sign-l" id="enq-title">{{ __('pages.equipment.enq_title') }}</h2><p class="lede" style="margin-top:20px">{{ __('pages.equipment.enq_lede') }}</p>
      @include('partials.direct-links', ['items' => ['whatsapp', 'catalogue']])</div>
    <div class="zone__form">@include('partials.enquiry-form')</div>
  </div>
</section>

</x-layout>
