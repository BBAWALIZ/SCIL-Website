{{-- One machine card. Needs $m (machine) and optional $heading (h3/h4). --}}
<a class="mcard footprint" href="{{ route('machine', ['slug' => $m['slug']]) }}">
  <div class="plate">
    <div class="mcard__img"><img class="photo-mult" src="{{ asset('assets/img/products/'.$m['image']) }}" alt="" loading="lazy" width="850" height="690"></div>
    <span class="mcard__fig">{{ $m['fig'] }}</span>
    <{{ $heading ?? 'h4' }}>{{ $m['name'] }}</{{ $heading ?? 'h4' }}>
    <p>{{ $m['summary'] }}</p>
  </div>
</a>
