from django.test import TestCase

from tests.models import Example

from django.core.management import call_command


class ModuleTest(TestCase):
    def test_001_basic(self):
        """Check for a basic functionality"""
        Example.objects.bulk_create([
            Example(name='привет %s' % i)
            for i in range(10000)
        ])
        instances = {
            e.id: e.name
            for e in Example.objects.all()
        }
        call_command('dumpdata', output='test-fixture.jsons')
        Example.objects.all().delete()
        call_command('loaddata', 'test-fixture.jsons')
        new_instances = {
            e.id: e.name
            for e in Example.objects.all()
        }
        self.assertEqual(len(instances), len(new_instances), 'Instances length not same: %s %s' % (len(instances), len(new_instances)))
        self.assertEqual(instances, new_instances)

    def test_002_from_string(self):
        Example.objects.bulk_create([
            Example(name='привет %s' % i)
            for i in range(10)
        ])
        original = {
            o.id: o.name
            for o in Example.objects.all()
        }
        from django.core import serializers
        serialized = serializers.serialize('json', Example.objects.all())
        deserialized = {
            o.object.id: o.object.name
            for o in serializers.deserialize('jsons', serialized)
        }
        self.assertEqual(original, deserialized)

    def test_003_from_bytes(self):
        Example.objects.bulk_create([
            Example(name='привет %s' % i)
            for i in range(10)
        ])
        original = {
            o.id: o.name
            for o in Example.objects.all()
        }
        from django.core import serializers
        serialized = serializers.serialize('json', Example.objects.all()).encode('utf-8')
        deserialized = {
            o.object.id: o.object.name
            for o in serializers.deserialize('jsons', serialized)
        }
        self.assertEqual(original, deserialized)
