@php
    $c = config('scil.contact');
    $idx = $stations->search(fn ($x) => $x['key'] === $m['station']);
@endphp
<x-layout :title="$m['name'].' · SCIL Machinery'" :desc="$m['name'].': '.$m['summary'].' '.$m['fig'].'.'" active="equipment">

<section class="page-head" style="padding-bottom:24px">
  <div class="wrap">
    <ol class="crumbs"><li><a href="{{ route('home') }}">{{ __('ui.home_crumb') }}</a></li><li><a href="{{ route('equipment') }}">{{ __('pages.equipment.crumb') }}</a></li><li><a href="{{ route('equipment') }}#{{ $station['key'] }}">{{ $station['no'] }} {{ $station['name'] }}</a></li></ol>
  </div>
</section>

<section class="wrap" style="padding-bottom:var(--space-section)">
  <div class="mdetail">
    <div class="mdetail__media"><div class="footprint"><div class="plate"><img class="photo-mult" src="{{ asset('assets/img/products/'.$m['image']) }}" alt="{{ $m['name'] }}" width="850" height="690"></div></div></div>
    <div class="mdetail__info">
      @if ($idx !== false)
        <nav class="lane-mini" aria-label="{{ __('pages.machine.position') }}">
          @foreach ($stations as $i => $x)
            <a href="{{ route('equipment') }}#{{ $x['key'] }}" title="{{ $x['name'] }}" class="{{ $i === $idx ? 'is-on' : ($i < $idx ? 'is-past' : '') }}">{{ $x['no'] }}<span> {{ $x['name'] }}</span></a>
          @endforeach
        </nav>
      @else
        <p class="meta" style="margin:0 0 24px">{{ __('pages.machine.water_note') }}</p>
      @endif
      <h1 class="sign-l">{{ $m['name'] }}</h1>
      <span class="mdetail__fig">{{ $m['fig'] }}</span>
      <p class="lede">{{ $m['summary'] }}</p>
      <div class="mdetail__actions">
        <a class="btn" href="{{ route('contact', ['machine' => $m['name']]) }}">{{ __('pages.machine.quote') }} <x-icon name="arrow"/></a>
        <a class="btn btn--plate" href="https://wa.me/{{ $c['whatsapp'] }}?text={{ rawurlencode(__('pages.machine.wa_text', ['name' => $m['name']])) }}" rel="noopener"><x-icon name="chat"/> {{ __('ui.whatsapp') }}</a>
      </div>
      <div class="body-copy prose" style="margin-top:36px">
        @foreach ($body as $b)
          @if ($b['type'] === 'list')
            <ul>@foreach ($b['items'] as $item)<li>{{ $item }}</li>@endforeach</ul>
          @elseif ($b['type'] === 'heading')
            <h3>{{ $b['text'] }}</h3>
          @else
            <p>{{ $b['text'] }}</p>
          @endif
        @endforeach
      </div>
      @if ($specs)
        @if ($specs['head'])
          <table class="specs specs--series"><caption>{{ $specs['caption'] }}</caption>
            <thead><tr>@foreach ($specs['head'] as $h)<th scope="col">{{ $h }}</th>@endforeach</tr></thead>
            <tbody>@foreach ($specs['rows'] as $r)<tr><th scope="row">{{ $r[0] }}</th>@foreach (array_slice($r, 1) as $cell)<td>{{ $cell }}</td>@endforeach</tr>@endforeach</tbody>
          </table>
        @else
          <table class="specs"><caption>{{ $specs['caption'] }}</caption>
            <tbody>@foreach ($specs['rows'] as [$k, $v])<tr><th scope="row">{{ $k }}</th><td>{{ $v }}</td></tr>@endforeach</tbody>
          </table>
        @endif
      @endif
      <p class="meta" style="margin-top:22px">{!! __('pages.machine.catalogue_note', ['url' => $c['catalogue']]) !!}</p>
    </div>
  </div>
</section>

@if ($siblings->isNotEmpty())
<section class="section" style="padding-top:0" aria-labelledby="sib"><div class="wrap">
  <div class="sec-head" style="margin-bottom:32px"><h2 class="sign-m" id="sib">{{ __('pages.machine.more_at', ['no' => $station['no'], 'name' => $station['name']]) }}</h2></div>
  <div class="cat-grid">@foreach ($siblings as $x) @include('partials.mcard', ['m' => $x, 'heading' => 'h3']) @endforeach</div>
</div></section>
@endif

</x-layout>
